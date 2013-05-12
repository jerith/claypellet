import struct

from PIL import Image

from .utils import Rect


HEADER_FORMAT = '<HHhhhh'
HEADER_FIELDS = ('row_size_bytes', 'info_flags', 'x', 'y', 'w', 'h')


class PebbleBitmap(object):
    def __init__(self, resource_data):
        self._resource_data = resource_data
        self._header = self._parse_header()
        self._data_start = struct.calcsize(HEADER_FORMAT)
        self.rect = Rect((self._header['x'], self._header['y']),
                         (self._header['w'], self._header['h']))
        self.row_size_bytes = self._header['row_size_bytes']
        self.info_flags = self._header['info_flags']
        self.image = self._load_data()

    def _parse_header(self):
        fields = struct.unpack_from(HEADER_FORMAT, self._resource_data)
        return dict(zip(HEADER_FIELDS, fields))

    def _load_data(self):
        offset = self._data_start

        return Image.fromstring(
            "1", self.rect.size, self._resource_data[offset:], "raw", "1;R",
            self._header['row_size_bytes'], 1)

    def get_image(self):
        return self.image.copy()

    def paste_to(self, dst, position, color):
        image = Image.new("LA", self.rect.size, color)
        image.putalpha(self.image)
        dst.paste(image, self.rect.move(position).origin)
