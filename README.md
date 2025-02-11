# `.bib` file generator with files

A Python script that generates a BibTeX file with various articles from arXiv.

The primary use for this generator is for making a large `.bib` file for testing the AI functionality in JabRef.

JabRef provides a script for generating large `.bib` files, but AI functionality operates on linked files.

## Features

- Searches arXiv for papers according to query.
- Fetches `title`, `author`, and `eprint` fields.
- Downloads PDF files.
- Forms a `.bib` file with ordinary count of entries.

## How to Run this Project

*I'll just paste a help message here* 😄

```
usage: main.py [-h] [--count COUNT] [--query QUERY] [--file FILE]

options:
  -h, --help     show this help message and exit
  --count COUNT  Count of entries to retrieve
  --query QUERY  Search query
  --file FILE    Path to generated file
```

Tip: to set the search query properly you can wrap it in double quotes. That way the shell will pass the series of words as one string.

## How this Project is Implemented

It's actually very simple, it has 2 external dependencies: one for arXiv API (for fetching papers), the other is for generating `.bib` entries. They are just combined.
