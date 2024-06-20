# Description
A Python script that generates a BibTeX file with various articles from arXiv.

It fetches only `title`, `author`, and `eprint` fields.

# Before running

Run this:

```
pip install -r -requirements.txt
```

The script relies on two packages:
- `arxiv`: searches for articles using arXiv API,
- `pybtex`: generates `.bib` files.

# Usage

*I'll just paste a help message here* 😄

```
usage: main.py [-h] [--count COUNT] [--query QUERY] [--file FILE]

options:
  -h, --help     show this help message and exit
  --count COUNT  Count of entries to retrieve
  --query QUERY  Set the search query
  --file FILE    Path to generated file
```

# Use in JabRef
The primary use for this generator is for making a large `.bib` file for testing the AI functionality in JabRef.

JabRef provides a script for generating large `.bib` files, but AI functionality operates on linked files.
