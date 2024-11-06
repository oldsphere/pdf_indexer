from setuptools import setup, find_packages

setup(
    name="pdf_indexer",
    author="Carlos Rubio",
    author_email="crubio.abujas@gmail.com",
    description="A module to add index to a pdf",
    url="https://github.com/oldsphere/pdf_indexer",
    packages=["PDFIndexer"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["pdf_indexer.py"],
)
