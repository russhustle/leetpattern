serve:
	uv run mkdocs serve


search:
	python utils/utils.py -s "def" -np

clean:
	find . -name ".DS_Store" -type f -delete
	find . -name "__pycache__" -type d -exec rm -r {} +
	find . -name "output" -type d -exec rm -r {} +
	find . -name "build" -type d -exec rm -r {} +

push:
	git add .
	git commit -m "Update"
	git push

sync:
	uv run python utils/sync.py

format:
	uv run pre-commit run --all-files

merge:
	git checkout main
	git merge dev
	git push origin main
	git checkout dev
	git merge main
	git push origin dev

build:
	uv run lpn generate

test:
	uv run pytest

run:
	$(MAKE) build
	$(MAKE) format || $(MAKE) format
	$(MAKE) clean
