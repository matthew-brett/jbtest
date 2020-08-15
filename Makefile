all: html sphinx

html:
	jupyter-book build .

sphinx:
	cd bare-sphinx && make html
