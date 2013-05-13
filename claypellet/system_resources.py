import json
from zipfile import ZipFile

from .resources import PebbleResources


class PebbleSystemResources(object):
    def __init__(self, firmware_path):
        self._firmware_path = firmware_path
        self._zipfile = ZipFile(firmware_path)
        self._manifest = json.loads(self._zipfile.read('manifest.json'))
        self._resource_data = self._zipfile.read('system_resources.pbpack')
        self.resources = PebbleResources(self._resource_data)
        self.resource_id_mapping = self.get_resource_id_mapping()

    def get_resource_id_mapping(self):
        resource_id_mapping = {}
        media = self._manifest['debug']['resourceMap']['media']
        file_id = 0
        for media_entry in media:
            file_id += 1
            resource_name = 'RESOURCE_ID_' + media_entry['defName']
            if media_entry['type'] == 'png-trans':
                resource_id_mapping[resource_name + '_WHITE'] = file_id
                file_id += 1
                resource_id_mapping[resource_name + '_BLACK'] = file_id
            else:
                resource_id_mapping[resource_name] = file_id
        return resource_id_mapping

    def verify_data(self):
        return self.resources.verify_data()

    def get_file_id(self, def_name):
        return self.resource_id_mapping[def_name]

    def get_chunk(self, file_id):
        return self.resources.get_chunk(file_id)
