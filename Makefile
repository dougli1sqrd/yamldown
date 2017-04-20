ENV=env/bin

all: yamldown.egg-info
	$(ENV)/mypy yamldown --strict-optional --ignore-missing-imports
	$(ENV)/nose2 tests -v

env:
	python3 -m venv env;

yamldown.egg-info: requirements.txt env
	$(ENV)/pip3 install -r requirements.txt
	$(ENV)/pip3 install --editable .
