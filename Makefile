# Copyright (c) KANO Computing Ltd. 2018
# Licensed under the GNU GPLv3 License
# Written by: Ioannis Valasakis <code@wizofe.uk>

PYTHON	?= python3
SETUP	:= setup.py

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}


isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint:
	flake8 --exclude=.tox

test: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

install:
	$(PYTHON) $(SETUP)  install --root $(DESTDIR)

clean:
	$(PYTHON) $(SETUP) clean --all

uninstall: clean
	-rm --force --recursive build/
	-rm --force --recursive dist/
	-rm --force --recursive *.egg-info
