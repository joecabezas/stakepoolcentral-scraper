import json

class Adalotl:
    POLICY_ID = '62ea7cb573306f6c272a2ff066679f2e4216270311d8e71b5f765251'

    def __init__(self, metadata):
        self.metadata = metadata

    @property
    def name(self):
        return self.metadata['name']

    @property
    def morph(self):
        return self.metadata['morph']

    @property
    def image(self):
        return self.metadata['image']

    @property
    def number(self):
        return self.metadata['number']

    @property
    def attributes(self):
        return self.metadata['attributes']

    def __str__(self):
        return json.dumps(self.metadata, indent=4)
