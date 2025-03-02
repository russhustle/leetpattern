serve:
	poetry run mkdocs serve


search:
	python utils/utils.py -s "def" -np

clean:
	find . -name ".DS_Store" -type f -delete
	find . -name "__pycache__" -type d -exec rm -r {} +
	find . -name "output" -type d -exec rm -r {} +

push:
	git add .
	git commit -m "Update"
	git push

sync:
	poetry run python utils/sync.py

format:
	poetry run pre-commit run --all-files || $(MAKE) format

build:
	poetry run python main.py

run:
	$(MAKE) build
	$(MAKE) format
	$(MAKE) clean
