serve:
    poetry run mkdocs serve

search:
    python utils.py -s "def" -np

clear:
    find . -name ".DS_Store" -type f -delete