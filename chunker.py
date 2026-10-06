from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter
)


CHUNKING_CONFIG = {
    "chunk_size": 1000,
    "chunk_overlap": 150,
}


def chunk_docs(documents):

    # Primary split: #
    header1_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header 1"),
        ]
    )

    # Used only when a # section is too large
    header2_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("##", "Header 2"),
        ]
    )

    # Used only when an individual section is still too large
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNKING_CONFIG["chunk_size"],
        chunk_overlap=CHUNKING_CONFIG["chunk_overlap"]
    )

    final_chunks = []

    for doc in documents:

        # -----------------------------------------
        # 1. Split document into # sections
        # -----------------------------------------

        sections = header1_splitter.split_text(
            doc.page_content
        )

        for section in sections:

            section.metadata.update(doc.metadata)

            parent_header = section.metadata.get("Header 1")

            # -----------------------------------------
            # 2. Keep small # sections together
            # -----------------------------------------

            if len(section.page_content) <= CHUNKING_CONFIG["chunk_size"]:

                section.page_content = (
                    f"# {parent_header}\n\n"
                    + section.page_content
                )

                final_chunks.append(section)

                continue

            # -----------------------------------------
            # 3. Large # section → split at ##
            # -----------------------------------------

            subsections = header2_splitter.split_text(
                section.page_content
            )

            for subsection in subsections:

                subsection.metadata.update(section.metadata)

                sub_header = subsection.metadata.get("Header 2")

                # -----------------------------------------
                # 4. Preserve both # and ## headings
                # -----------------------------------------

                headings = ""

                if parent_header:
                    headings += f"# {parent_header}\n\n"

                if sub_header:
                    headings += f"## {sub_header}\n\n"

                subsection.page_content = (
                    headings + subsection.page_content
                )

                # -----------------------------------------
                # 5. Keep small ## sections together
                # -----------------------------------------

                if len(subsection.page_content) <= CHUNKING_CONFIG["chunk_size"]:

                    final_chunks.append(subsection)

                # -----------------------------------------
                # 6. Very large ## section → recursive split
                # -----------------------------------------

                else:

                    small_chunks = recursive_splitter.split_documents(
                        [subsection]
                    )

                    final_chunks.extend(small_chunks)

    print(f"Total chunks created: {len(final_chunks)}")

    return final_chunks