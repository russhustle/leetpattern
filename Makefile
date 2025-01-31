serve:
	poetry run mkdocs serve


search:
	python utils/utils.py -s "def" -np

clean:
	find . -name ".DS_Store" -type f -delete
# delete __pycache__ folders
	find . -name "__pycache__" -type d -exec rm -r {} +

push:
	git add .
	git commit -m "Update"
	git push

sync:
	poetry run python utils/sync.py
