ENV=env/bin

all: yamldown.egg-info
	$(ENV)/mypy yamldown --strict-optional --ignore-missing-imports
	$(ENV)/nose2 tests -v

env:
	python3 -m venv env;

yamldown.egg-info: requirements.txt env
	$(ENV)/pip3 install -r requirements.txt
	$(ENV)/pip3 install --editable .

cleandist:
	rm dist/* || true

TAG = v$(shell python setup.py --version)
versioning:
	git checkout master
	git add setup.py
	git commit --message="Upgrade to $(TAG)"
	git push origin master
	git tag --annotate $(TAG) -f --message="Upgrade to $(TAG)"
	git push --tags

USER ?= $(LOGNAME)
release: cleandist
	python setup.py sdist bdist_wheel bdist_egg
	twine upload --repository-url https://upload.pypi.org/legacy/ --username $(USER) dist/*

test_release: cleandist
	python setup.py sdist bdist_wheel bdist_egg
	twine upload --repository-url https://test.pypi.org/legacy/ --username $(USER) dist/*
