import struct


FONTINFO_FORMAT = '<BBHH'
FONTINFO_FIELDS = ('version', 'max_height', 'glyph_count', 'wildcard_char')

GLYPH_HEADER_FORMAT = '<BBbb3Bb'
GLYPH_HEADER_FIELDS = (
    'width', 'height', 'offset_left', 'offset_top', '_', '_', '_', 'advance')


class PebbleFont(object):
    def __init__(self, resource_data):
        self.resource_data = resource_data
        self.fontinfo = self.parse_fontinfo()
        assert self.fontinfo['version'] == 1
        self.glyph_offsets = self.parse_offset_table()
        self.glyph_table_start = (struct.calcsize(FONTINFO_FORMAT) +
                                  4 * self.fontinfo['glyph_count'])
        self.glyphs = {}

    def parse_fontinfo(self):
        fields = struct.unpack_from(FONTINFO_FORMAT, self.resource_data)
        return dict(zip(FONTINFO_FIELDS, fields))

    def parse_offset_table(self):
        offset = struct.calcsize(FONTINFO_FORMAT)
        glyph_offsets = {}

        for i in range(self.fontinfo['glyph_count']):
            codepoint, glyph_offset = struct.unpack_from(
                '<HH', self.resource_data[offset:])
            offset += 4
            glyph_offsets[codepoint] = glyph_offset

        return glyph_offsets

    def parse_glyph(self, codepoint):
        table_offset = self.glyph_offsets[codepoint]
        offset = self.glyph_table_start + table_offset * 4
        header = dict(zip(GLYPH_HEADER_FIELDS,
                          struct.unpack_from(GLYPH_HEADER_FORMAT,
                                             self.resource_data[offset:])))
        bmsize = header['width'] * header['height']
        bmoffset = offset + struct.calcsize(GLYPH_HEADER_FORMAT)
        bitmap = []
        while len(bitmap) < bmsize:
            word = struct.unpack_from('<I', self.resource_data[bmoffset:])[0]
            for i in range(32):
                b = (word >> i) % 2
                bitmap.append({
                    0: '\x00\x00\x00\x00',
                    1: '\xff\xff\xff\xff',
                }[b])
            bmoffset += 4

        header.pop('_')
        header['data_string'] = ''.join(bitmap)[:bmsize * 4]

        return header

    def get_glyph(self, codepoint):
        if codepoint not in self.glyphs:
            self.glyphs[codepoint] = self.parse_glyph(codepoint)
        return self.glyphs[codepoint]
