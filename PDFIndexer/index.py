from PyPDF2 import PdfReader, PdfWriter
from dataclasses import dataclass
from typing import List, Union
from pprint import pprint

Path = str
nullInt = Union[int, None]

PAGE_DELIMITER = "..."
LEVEL_DELIMITER = "    "
LAST = -1


@dataclass
class IndexItem:
    level: int
    text: str
    page: int


def add_index(input: Path, output: Path, index: List[IndexItem]):
    writer = generate_pdf_copy(input)
    current_level = -1
    bookmark_hierarquy = []
    bookmark = None
    for item in index:
        if item.level > current_level:
            current_level = item.level
            bookmark_hierarquy.append(bookmark)

        if item.level < current_level:
            current_level = item.level
            bookmark_hierarquy.pop()

        bookmark = writer.add_outline_item(
            title=item.text, page_number=item.page, parent=bookmark_hierarquy[LAST]
        )

    with open(output, "wb") as f:
        writer.write(f)


def add_index_offset(index: List[IndexItem], offset: int) -> List[IndexItem]:
    new_index = index.copy()
    for item in new_index:
        item.page += offset
    return new_index


def generate_pdf_copy(input: Path) -> PdfWriter:
    reader = PdfReader(input)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    return writer


def read_index(file: Path) -> List[IndexItem]:
    with open(file, "r") as f:
        content = f.read()
    lines_raw = content.split("\n")
    lines_no_empty = filter(is_not_empty, lines_raw)
    lines = filter(is_not_comment, lines_no_empty)
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> IndexItem:
    text, page = line.strip().split(PAGE_DELIMITER)
    return IndexItem(
        level=line.count(LEVEL_DELIMITER),
        text=text,
        page=int(page),
    )


def show_tree(index: List[IndexItem]):
    current_level = 0
    current_path = []
    prev_item = IndexItem(0, "", 0)
    show = lambda: print("->".join(current_path + [item.text]))

    for item in index:
        if item.level == current_level:
            show()

        if item.level > current_level:
            current_level = item.level
            current_path.append(prev_item.text)
            show()

        if item.level < current_level:
            current_level = item.level
            current_path.pop()
            show()

        prev_item = item


def is_not_empty(line: str) -> bool:
    return not is_empty(line)


def is_empty(line: str) -> bool:
    if len(line) == 0:
        return True
    return not line.strip()[0] != "\n"


def is_not_comment(line: str) -> bool:
    return line.strip()[0] != "#"
