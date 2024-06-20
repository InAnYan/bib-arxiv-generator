import argparse
import arxiv
from pybtex.database import BibliographyData, Entry

parser = argparse.ArgumentParser()

parser.add_argument(
    "--count", type=int, help="Count of entries to retrieve", default=10
)

parser.add_argument("--query", type=str, help="Search query", default="AI RAG LLM")

parser.add_argument(
    "--file", type=str, help="Path to generated file", default="result.bib"
)

args = parser.parse_args()

client = arxiv.Client()

search = arxiv.Search(query=args.query, max_results=args.count)

results = client.results(search)

counter = 0

with open(args.file, "w", encoding="utf-8") as f:
    bib = BibliographyData(
        {
            f"result{i + 1}": Entry(
                "article",
                [
                    (
                        "author",
                        ", ".join(map(lambda author: author.name, result.authors)),
                    ),
                    ("title", result.title),
                    ("eprint", result.pdf_url[len("http://arxiv.org/pdf/") :]),
                ],
            )
            for i, result in enumerate(results)
        }
    )

    bib_str = bib.to_string("bibtex")
    f.write(bib_str)
