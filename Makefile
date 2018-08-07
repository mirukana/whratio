# Copyright 2018 miruka
# This file is part of whratio, licensed under LGPLv3.

PYTHON = python3
PIP    = pip3

ARCHIVE_FORMATS = bztar,zip
INSTALL_FLAGS   = --user --editable

.PHONY: all clean dist install upload test


all: clean dist install

clean:
	find . -name '__pycache__' -exec rm -Rfv {} +
	find . -name '*.pyc'       -exec rm -Rfv {} +
	find . -name '*.egg-info'  -exec rm -Rfv {} +
	rm -Rfv build dist

dist: clean
	@echo
	${PYTHON} setup.py sdist --format ${ARCHIVE_FORMATS}
	@echo
	${PYTHON} setup.py bdist_wheel

install: clean
	@echo
	${PIP} install ${INSTALL_FLAGS} .


upload: dist
	@echo
	twine upload dist/*


test:
	-pylint --output-format colorized whratio
	@echo
	cloc --vcs git --ignore-whitespace whratio
