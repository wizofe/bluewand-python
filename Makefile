
PROJECT_NAME := $(shell python setup.py --name)
PROJECT_VERSION := $(shell python setup.py --version)

SHELL := /bin/bash
BOLD := \033[1m
DIM := \033[2m
RESET := \033[0m

.PHONY: all
all: uninstall install clean

.PHONY: install
install:
	@echo -e "$(BOLD)installing $(PROJECT_NAME) $(PROJECT_VERSION)$(RESET)"
	@echo -e -n "$(DIM)"
	@pip install .
	@echo -e -n "$(RESET)"

.PHONY: uninstall
uninstall:
	@echo -e "$(BOLD)uninstalling '$(PROJECT_NAME)'$(RESET)"
	-@pip uninstall -y $(PROJECT_NAME) 2> /dev/null

.PHONY: test
test: uninstall install
	@echo -e "$(BOLD)running test units for $(PROJECT_NAME) $(PROJECT_VERSION)$(RESET)"
	@python -m unittest discover -s tests -p 'tests_*.py' --verbose
	@rm -rf tests/*.pyc

.PHONY: lint
lint:
	@echo -e "$(BOLD)analyzing code for $(PROJECT_NAME) $(PROJECT_VERSION)$(RESET)"
	-@pylint bin/* lib/**/*.py \
		--output-format text --reports no \
		--msg-template "{path}:{line:04d}:{obj} {msg} ({msg_id})" \
		| sort | awk \
			'/[RC][0-9]{4}/ {print "\033[2m" $$0 "\033[0m"};\
			 /[EF][0-9]{4}/ {print "\033[1m" $$0 "\033[0m"};\
			 /W[0-9]{4}/ {print};'

.PHONY: doc
doc:
	@echo -e "$(BOLD)building documentation for $(PROJECT_NAME) $(PROJECT_VERSION)$(RESET)"
	@echo -e -n "$(DIM)"
	@cd doc && $(MAKE) html
	@echo -e -n "$(RESET)"

.PHONY: dist
dist:
	@echo -e "$(BOLD)packaging $(PROJECT_NAME) $(PROJECT_VERSION)$(RESET)"
	@echo -e -n "$(DIM)"
	@python setup.py sdist --formats=zip --dist-dir=dist
	@echo -e -n "$(RESET)"

.PHONY: clean
clean:
	@echo -e "$(BOLD)cleaning $(PROJECT_NAME) $(PROJECT_VERSION) repository$(RESET)"
	@rm -rf build dist $(PROJECT_NAME).egg-info
