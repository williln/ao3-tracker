import re
import pathlib

from AO3 import Work
from AO3.utils import workid_from_url

root = pathlib.Path(__file__).parent.resolve()

index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s


if __name__ == "__main__":
    # Get file
    file = root / "generated.txt"
    contents = file.open().read()
    link = contents.split()[0]

    # Get data from AO3
    fic_id = workid_from_url(link)
    fic = Work(fic_id)

    # Process data
    fic_data = fic.metadata
    title = fic_data["title"]
    id = fic_data["id"]
    rating = fic_data["rating"]
    word_count = fic_data["words"]
    warnings = fic_data["warnings"]
    complete = fic_data["complete"]
    authors = fic_data["authors"]
    fandoms = fic_data["fandoms"]
    relationships = fic_data["relationships"]
    characters = fic_data["characters"]
    tags = fic_data["tags"]
    raw_summary = fic_data["summary"]

    # Massage summary
    summary_pieces = raw_summary.split("\n")
    summary = "".join(summary_pieces)
    # Replace double quotes with single quotes so that I can put the whole thing in quotes later.
    summary = summary.replace('"', "'")

    # Get a slug for the new filename
    to_slugify = [title, "by"]
    to_slugify += authors
    to_slugify.append(str(id))
    slug = slugify(" ".join(to_slugify))

    # Open the file and write the yaml
    f = open(f"fics/{slug}.yml", "a")
    index = ["---"]
    index.append(f"title: {title}")
    index.append(f"id: {id}")
    index.append(f"word_count: {word_count}")
    index.append(f"complete: {complete}")
    index.append(f"read: False")
    index.append(f"rating: {rating}")
    index.append(f'summary: "{summary}"')

    if len(warnings) > 1:
        index.append("warnings:")
        for warning in warnings:
            index.append(f"  - {warning}")
    elif len(warnings) == 1:
        index.append(f"warnings: {warnings[0]}")
    else:
        index.append("warnings:")

    if len(authors) > 1:
        index.append("authors:")
        for author in authors:
            index.append(f"  - {author}")
    elif len(authors) == 1:
        index.append(f"authors: {authors[0]}")
    else:
        index.append("authors:")

    if len(fandoms) > 1:
        index.append("fandoms:")
        for fandom in fandoms:
            index.append(f"  - {fandom}")
    elif len(fandoms) == 1:
        index.append(f"fandoms: {fandoms[0]}")
    else:
        index.append("fandoms:")

    if len(relationships) > 1:
        index.append("relationships:")
        for relationship in relationships:
            index.append(f"  - {relationship}")
    elif len(relationships) == 1:
        index.append(f"relationships: {relationships[0]}")
    else:
        index.append("relationships:")

    if len(characters) > 1:
        index.append("characters:")
        for character in characters:
            index.append(f"  - {character}")
    elif len(characters) == 1:
        index.append(f"characters: {characters[0]}")
    else:
        index.append("characters:")

    if len(tags) > 1:
        index.append("tags:")
        for tag in tags:
            index.append(f"  - {tag}")
    elif len(tags) == 1:
        index.append(f"tags: {tags[0]}")
    else:
        index.append("tags:")

    index.append("---")

    # Add the content to the file and close it
    index_txt = "\n".join(index).strip()
    f.write(index_txt)
    f.close()
