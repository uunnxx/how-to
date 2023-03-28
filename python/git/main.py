import os
import collections
import hashlib
import struct
import zlib


def write_file(*args, **kwargs):
    return 0


def read_file(*args, **kwargs):
    return 0


def init(repo):
    """Create directory for repo and initialize .git direcotry."""

    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.git'))
    for name in ['objects', 'refs', 'refs/heads']:
        os.mkdir(os.path.join(repo, '.git', name))
    write_file(os.path.join(repo, '.git', 'HEAD'),
               b'ref: refs/heads/main')
    print(f"initialized empty repository: {repo}")


def hash_object(data, obj_type, write=True):
    """
    Compute hash of object data of given type and wirte to object store
    if 'write' is True. Return SHA-1 object hash as hex string.
    """
    header = f"{obj_type} {len(data)}".encode()
    full_data = header + b'\x00' + data
    sha1 = hashlib.sha1(full_data).hexdigest()
    if write:
        path = os.path.join('.git', 'objects', sha1[:2], sha1[2:])
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            write_file(path, zlib.compress(full_data))

    return sha1


# Data for one entry in the git index (.git/index)
IndexEntry = collections.namedtuple('IndexEntry', [
    'ctime_s', 'ctime_n', 'mtime_s', 'mtime_n', 'dev', 'ino', 'mode'
    'uid', 'gid', 'size', 'sha1', 'flags', 'path'
])


def read_index():
    """Read git index file and return list of IndexEntry objects."""

    try:
        data = read_file(os.path.join('.git', 'index'))
    except FileNotFoundError:
        return []

    digest = hashlib.sha1(data[:-20]).digest()
    assert digest == data[-20:], 'invalid index checksum'

    signature, version, num_entries = struct.unpack('!4sLL', data[:12])
    assert signature == b'DIRC', \
        f'invalid index signature {signature}'
    assert version == 2, f'unknown index version {version}'

    entry_data = data[12:-20]
    entries = []
    i = 0
    while i + 62 < len(entry_data):
        fields_end = i + 62
        fields = struct.unpack('!LLLLLLLLLL20sH',
                               entry_data[i:fields_end])
        path_end = entry_data.index(b'\x00', fields_end)
        path = entry_data[fields_end:path_end]
        entry = IndexEntry(*(fields + (path.decode(),)))
        entries.append(entry)
        entry_len = ((62 + len(path) + 8) // 8) * 8
        i += entry_len

    assert len(entries) == num_entries
    return entries


def write_tree():
    """Write a tree object from the current index entries."""

    tree_entries = []
    for entry in read_index():
        assert '/' not in entry.path, \
            'currently only supports a single, top-level directory'
