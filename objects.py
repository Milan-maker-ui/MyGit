import hashlib
import zlib
import os
import time


class GitObject:
    def __init__(self, data):
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha1 = hashlib.sha1()
        sha1.update(self.data)
        return sha1.hexdigest()

    def compress(self):
        return zlib.compress(self.data)

    def save(self, repo_path):
        obj_dir = os.path.join(repo_path, "objects", self.hash[:2])

        os.makedirs(obj_dir, exist_ok=True)

        obj_path = os.path.join(obj_dir, self.hash[2:])

        with open(obj_path, "wb") as f:
            f.write(self.compress())


class Blob(GitObject):
    def __init__(self, data):
        header = f"blob {len(data)}".encode() + b'\\0'
        super().__init__(header + data)


class Tree(GitObject):
    def __init__(self, entries):
        tree_data = b''

        for mode, name, obj_hash in entries:
            tree_data += (
                f"{mode:o} {name}".encode()
                + b'\\0'
                + bytes.fromhex(obj_hash)
            )

        header = f"tree {len(tree_data)}".encode() + b'\\0'

        super().__init__(header + tree_data)


class Commit(GitObject):
    def __init__(self, tree_hash, parent_hashes, author, message):
        timestamp = int(time.time())

        content = f"tree {tree_hash}\\n"

        for parent in parent_hashes:
            content += f"parent {parent}\\n"

        content += f"author {author} {timestamp} +0000\\n"
        content += f"committer {author} {timestamp} +0000\\n\\n"
        content += message + "\\n"

        data = content.encode()

        header = f"commit {len(data)}".encode() + b'\\0'

        super().__init__(header + data)