import os
import struct


class Index:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.entries = {}

        self.index_path = os.path.join(repo_path, "index")

        self.load()

    def load(self):
        if not os.path.exists(self.index_path):
            return

        with open(self.index_path, "rb") as f:
            data = f.read()

        if data[:4] != b'DIRC':
            return

        entry_count = struct.unpack(">I", data[8:12])[0]

        offset = 12

        for _ in range(entry_count):
            mode = struct.unpack(">I", data[offset:offset+4])[0]
            offset += 4

            hash_bytes = data[offset:offset+20]
            obj_hash = hash_bytes.hex()
            offset += 20

            path_length = struct.unpack(">H", data[offset:offset+2])[0]
            offset += 2

            path = data[offset:offset+path_length].decode()
            offset += path_length

            self.entries[path] = (mode, obj_hash)

    def add(self, path, mode, obj_hash):
        self.entries[path] = (mode, obj_hash)

    def save(self):
        header = b'DIRC' + struct.pack(">II", 2, len(self.entries))

        entries_data = b''

        for path in sorted(self.entries.keys()):
            mode, obj_hash = self.entries[path]

            entry = struct.pack(">I", mode)

            entry += bytes.fromhex(obj_hash)

            path_bytes = path.encode()

            entry += struct.pack(">H", len(path_bytes))

            entry += path_bytes

            entries_data += entry

        with open(self.index_path, "wb") as f:
            f.write(header + entries_data)