.PHONY: clean
clean:
	if [ -d build ]; then rm -rf build; fi
	if [ -d dist ]; then rm -rf dist; fi
	if [ -d pureport_python.egg-info ]; then rm -rf pureport_python.egg-info; fi
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	cd docs && make clean
	coverage erase
	if [ -d .tox ]; then rm -rf .tox; fi

test: clean
	tox

.PHONY: docs
docs: 
	cd docs && make clean
	cd docs && sphinx-apidoc ../pureport -o . -f
	cd docs && PUREPORT_AUTOMAKE_BINDINGS=0 make html


build: clean
	python setup.py sdist bdist_wheel
