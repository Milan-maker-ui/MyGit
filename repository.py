import os
import struct

from mygit.index import Index
from mygit.objects import Blob, Tree, Commit


class GitRepository:
    def __init__(self, path):
        self.path = path
        self.index = Index(path)

    @classmethod
    def init(cls, path):
        repo_path = os.path.join(path, ".mygit")

        os.makedirs(os.path.join(repo_path, "objects"), exist_ok=True)
        os.makedirs(os.path.join(repo_path, "refs", "heads"), exist_ok=True)

        with open(os.path.join(repo_path, "HEAD"), "w") as f:
            f.write("ref: refs/heads/master\n")

        return cls(repo_path)

    def add(self, file_path):
        abs_path = os.path.abspath(file_path)

        with open(abs_path, "rb") as f:
            content = f.read()

        blob = Blob(content)
        blob.save(self.path)

        stat = os.stat(abs_path)

        self.index.add(
            file_path,
            stat.st_mode,
            blob.hash
        )

        self.index.save()

        return blob.hash

    def commit(self, message, author):
        entries = []

        for path, (mode, obj_hash) in self.index.entries.items():
            entries.append((mode, path, obj_hash))

        tree = Tree(entries)
        tree.save(self.path)

        commit = Commit(
            tree.hash,
            [],
            author,
            message
        )

        commit.save(self.path)

        head_path = os.path.join(
            self.path,
            "refs",
            "heads",
            "master"
        )

        with open(head_path, "w") as f:
            f.write(commit.hash)

        return commit.hash