# MyGit

A lightweight Git implementation written in Python that demonstrates the core concepts behind Git's version control system. This project implements essential Git features such as repository initialization, object storage, staging files, and creating commits.

---

## Features

- Initialize a Git repository
- Blob object creation
- SHA-1 object hashing
- Object compression using zlib
- Store Git objects
- Staging area (Index)
- Create commits
- Tree object generation
- Command Line Interface (CLI)
- Cross-platform (Windows/Linux/macOS)

---

## Technologies Used

- Python 3.10+
- hashlib
- zlib
- os
- struct
- argparse
- pytest

---

## Repository Structure After Initialization

```
.mygit/
│
├── objects/
├── refs/
│   └── heads/
├── HEAD
└── index
```

---

## How It Works

### Repository Initialization

Creates a hidden `.mygit` directory containing:

- objects/
- refs/
- HEAD
- index

---

### Blob Objects

Each file is stored as a Blob object.

```
File
   ↓
SHA-1 Hash
   ↓
Compressed
   ↓
Stored in .mygit/objects/
```

---

### Tree Objects

A Tree object stores directory information and references Blob objects.

---

### Commit Objects

Each commit contains:

- Tree Hash
- Parent Commit
- Author
- Commit Message
- Timestamp

---

## Running Tests

```bash
pytest
```

---

## Example Workflow

```bash
python -m mygit.cli init

python -m mygit.cli add examples/sample.txt

python -m mygit.cli commit -m "First Commit"
```

---

## Future Improvements

- Branch support
- Checkout
- Merge
- Log command
- Status command
- Diff command
- Remote repositories
- Clone command
- Push & Pull
- Tag support
- Ignore files
- Restore command

---

## Learning Objectives

This project demonstrates:

- Version Control Systems
- Git Internals
- SHA-1 Hashing
- File Compression
- Object-Oriented Programming
- File System Operations
- Command Line Interface Design
- Data Structures
- Python Programming

---

