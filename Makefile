serve:
    poetry run mkdocs serve

search:
    python utils.py -s "def" -np

clear:
    find . -name ".DS_Store" -type f -delete

push:
    # tag
    git tag -a v0.1.10 -m "Release v0.1.10"