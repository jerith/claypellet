import struct

from PIL import Image

from .utils import Rect


FONTINFO_FORMAT = '<BBHH'
FONTINFO_FIELDS = ('version', 'max_height', 'glyph_count', 'wildcard_char')

GLYPH_HEADER_FORMAT = '<BBbb3Bb'
GLYPH_HEADER_FIELDS = (
    'width', 'height', 'offset_left', 'offset_top', '_', '_', '_', 'advance')


class PebbleFont(object):
    def __init__(self, resource_data):
        self._resource_data = resource_data
        self.fontinfo = self._parse_fontinfo()
        assert self.fontinfo['version'] == 1
        self._glyph_offsets = self._parse_offset_table()
        self._glyph_table_start = (struct.calcsize(FONTINFO_FORMAT) +
                                   4 * self.fontinfo['glyph_count'])
        self._glyphs = {}
        self.max_height = self.fontinfo['max_height']

    def _parse_fontinfo(self):
        fields = struct.unpack_from(FONTINFO_FORMAT, self._resource_data)
        return dict(zip(FONTINFO_FIELDS, fields))

    def _parse_offset_table(self):
        offset = struct.calcsize(FONTINFO_FORMAT)
        glyph_offsets = {}

        for i in range(self.fontinfo['glyph_count']):
            codepoint, glyph_offset = struct.unpack_from(
                '<HH', self._resource_data[offset:])
            offset += 4
            glyph_offsets[codepoint] = glyph_offset

        return glyph_offsets

    def _parse_glyph(self, codepoint):
        table_offset = self._glyph_offsets[codepoint]
        offset = self._glyph_table_start + table_offset * 4
        header = dict(zip(GLYPH_HEADER_FIELDS,
                          struct.unpack_from(GLYPH_HEADER_FORMAT,
                                             self._resource_data[offset:])))
        bmsize = header['width'] * header['height']
        bmoffset = offset + struct.calcsize(GLYPH_HEADER_FORMAT)
        bitmap = []
        while len(bitmap) < bmsize:
            word = struct.unpack_from('<I', self._resource_data[bmoffset:])[0]
            for i in range(32):
                b = (word >> i) % 2
                bitmap.append({
                    0: '\x00',
                    1: '\xff',
                }[b])
            bmoffset += 4

        header.pop('_')
        return header, ''.join(bitmap)[:bmsize]

    def get_glyph(self, ch):
        if ch not in self._glyphs:
            codepoint = ord(ch)
            header, bitmap = self._parse_glyph(codepoint)
            self._glyphs[ch] = PebbleGlyph(codepoint, header, bitmap)
        return self._glyphs[ch]


class PebbleGlyph(object):
    def __init__(self, codepoint, header, bitmap):
        self.codepoint = codepoint
        self._header = header
        self.advance = header['advance']
        self.rect = Rect((header['offset_left'], header['offset_top']),
                         (header['width'], header['height']))

        if self.rect.area == 0:
            # Special-case for empty glyphs.
            self.image = None
        else:
            self.image = Image.fromstring(
                "L", self.rect.size, bitmap, "raw", "L", 0, 1)

    def paste_to(self, dst, position, color):
        if self.image is not None:
            image = Image.new("LA", self.rect.size, color)
            image.putalpha(self.image)
            dst.paste(image, self.rect.move(position).origin)
