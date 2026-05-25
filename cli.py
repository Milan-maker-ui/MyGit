import argparse
import os

from mygit.repository import GitRepository


def find_repo():
    current = os.getcwd()

    while True:
        repo = os.path.join(current, ".mygit")

        if os.path.exists(repo):
            return repo

        parent = os.path.dirname(current)

        if parent == current:
            break

        current = parent

    return None


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("files", nargs="+")

    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("-m", "--message", required=True)

    args = parser.parse_args()

    if args.command == "init":
        GitRepository.init(os.getcwd())
        print("Repository initialized")

    elif args.command == "add":
        repo = GitRepository(find_repo())

        for file in args.files:
            obj_hash = repo.add(file)
            print(f"Added {file}: {obj_hash[:7]}")

    elif args.command == "commit":
        repo = GitRepository(find_repo())

        commit_hash = repo.commit(
            args.message,
            "Milan <milan@example.com>"
        )

        print(f"Commit created: {commit_hash[:7]}")


if __name__ == "__main__":
    main()