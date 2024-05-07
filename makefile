.PHONY: install
install:
	python -m pip install -r requirements.txt

README.md:
	python update_readme.py > README.md
