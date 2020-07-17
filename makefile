virtualenv:
	python -m pip install -r requirements.txt

readme:
	python update_readme.py > README.md
