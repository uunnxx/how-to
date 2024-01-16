import json
import xml.etree.ElementTree as elem


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = str(song_id)
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        serializer = self._get_serializer(format)

        return serializer(song)

    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }

        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_info = elem.Element('song', attrib={'id': song.song_id})
        title = elem.SubElement(song_info, 'title')
        title.text = song.title
        artist = elem.SubElement(song_info, 'artist')
        artist.text = song.artist

        return elem.tostring(song_info, encoding='unicode')


song = Song(1, 'Water of Love', 'Dire Straits')
serializer = SongSerializer()

print(serializer.serialize(song, 'JSON'))
print(serializer.serialize(song, 'XML'))


class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = elem.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = elem.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return elem.tostring(self._element, encoding='unicode')


