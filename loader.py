from pathlib import Path
from typing import List
import yaml
import re
from langchain_core.documents import Document

knowledge_base_path = Path("knowledge_base")


def fetch_documents():

    documents = []

    for folder in knowledge_base_path.iterdir():

        for file in folder.glob("*.md"):

            with open(file, "r", encoding="utf-8") as f:

                text = f.read()

            parts = text.split("---", maxsplit=2)

            if len(parts) != 3:
                raise ValueError(
                    f"{file.name} does not contain valid YAML front matter."
                )

            metadata = yaml.safe_load(parts[1])
            metadata["source_file"] = file.name

            page_content = parts[2].strip()
            # Remove standalone --- separators
            page_content = re.sub(
                r"(?m)^\s*---\s*$",
                "",
                page_content
            ).strip()


            documents.append(
                Document(
                    page_content=page_content,
                    metadata=metadata
                )
            )


    return documents