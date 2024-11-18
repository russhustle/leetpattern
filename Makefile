serve:
	poetry run mkdocs serve


search:
	python utils/utils.py -s "def" -np

clean:
	find . -name ".DS_Store" -type f -delete
# delete __pycache__ folders
	find . -name "__pycache__" -type d -exec rm -r {} +

push:
	# tag
	git tag -a v0.1.10 -m "Release v0.1.10"
	git push origin v0.1.10
