# Cribbed from Simon Willison: https://github.com/simonw/til/blob/0abdc32464f1bc726abebdbc147b945d22bae7a8/update_readme.py
"Run this after build_database.py - it needs ficnotes.db"
import pathlib
import sqlite_utils
import sys
import re

root = pathlib.Path(__file__).parent.resolve()

index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)

if __name__ == "__main__":
    # Get the link from the argument
    if "--link" in sys.argv:
        print(f"This is the link: {sys.argv[:-1]}")

    # Pass it to the AO3 work getter

    # AO3 work getter goes to AO3 and returns data as JSON

    # Parse the title and author into a markdown file

    # Check fics/ to see if we have that markdown file

    # If yes, skip

    # If no, create a new file using that slug

    # Cycle through the JSON and fill in the markdown file

    # All done
    # db = sqlite_utils.Database(root / "ficnotes.db")
    # by_topic = {}
    # for row in db["ficnotes"].rows_where(order_by="created_utc"):
    #     by_topic.setdefault(row["topic"], []).append(row)

    # index = ["<!-- index starts -->"]

    # # Alphabetize the topics
    # topics = list(by_topic.keys())
    # topics.sort()

    # for topic in topics:
    #     # Set up the heading
    #     index.append("### {}\n".format(topic))

    #     # Set up the table
    #     index.append("| Title | Pairing | Status | Last Updated |")
    #     index.append("| ----- | ----- | ----- | ----- |")

    #     # Go through the items
    #     rows = by_topic[topic]
    #     for row in rows:
    #         index.append(
    #             "| [{title}]({url})<br />{summary} | {pairing} | {status} | {date} |".format(
    #                 date=row["created"].split("T")[0], **row
    #             )
    #         )
    #     index.append("")
    # if index[-1] == "":
    #     index.pop()
    # index.append("<!-- index ends -->")

    # if "--rewrite" in sys.argv:
    #     readme = root / "README.md"
    #     index_txt = "\n".join(index).strip()
    #     readme_contents = readme.open().read()
    #     readme.open("w").write(index_re.sub(index_txt, readme_contents))
    # else:
    #     print("\n".join(index))
