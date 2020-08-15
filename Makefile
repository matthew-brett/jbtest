all: html sphinx

SPHINX_DIR=bare-sphinx

html:
	jupyter-book build .

sphinx:
	cd $(SPHINX_DIR) && make html

clean:
	rm -rf _build
	cd $(SPHINX_DIR) && make clean
