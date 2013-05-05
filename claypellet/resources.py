import struct


MANIFEST_FORMAT = '<III16s'
MANIFEST_FIELDS = ('num_files', 'crc', 'timestamp', 'readable_version')

TABLE_ENTRY_FORMAT = '<IIII'
TABLE_ENTRY_FIELDS = ('file_id', 'start', 'length', 'crc')


def parse_manifest(resource_data):
    fields = struct.unpack_from(MANIFEST_FORMAT, resource_data)
    return dict(zip(MANIFEST_FIELDS, fields))


def parse_table(resource_data, manifest):
    offset = struct.calcsize(MANIFEST_FORMAT)
    table = []
    for i in range(manifest['num_files']):
        fields = struct.unpack_from(TABLE_ENTRY_FORMAT, resource_data[offset:])
        table.append(dict(zip(TABLE_ENTRY_FIELDS, fields)))
        offset += struct.calcsize(TABLE_ENTRY_FORMAT)
    return table


class PebbleResources(object):
    def __init__(self, resource_data):
        self.resource_data = resource_data
        self.manifest = parse_manifest(resource_data)
        self.table = parse_table(resource_data, self.manifest)
        self.data_offset = self.guess_data_start()
        self.chunk_metadata = dict((entry['file_id'], entry)
                                   for entry in self.table)
        self.chunks = {}

    def guess_data_start(self):
        # Start by assuming we have 256 table entries.
        table_entries_start = (struct.calcsize(MANIFEST_FORMAT) +
                               256 * struct.calcsize(TABLE_ENTRY_FORMAT))
        # Then count backwards by data length.
        data_length_start = (len(self.resource_data) -
                             sum(entry['length'] for entry in self.table))
        if table_entries_start != data_length_start:
            print "WARNING: Two methods of finding data start differ."
        return data_length_start

    def verify_data(self):
        from stm32_crc import crc32
        data_crc = crc32(self.resource_data[self.data_offset:])
        assert data_crc == self.manifest['crc']
        for entry in self.table:
            chunk_crc = crc32(self.get_chunk(entry['file_id']))
            assert chunk_crc == entry['crc']

    def get_chunk(self, file_id):
        md = self.chunk_metadata[file_id]
        start = self.data_offset + md['start']
        end = start + md['length']
        return self.resource_data[start:end]
