.PHONY: test coverage

test:
	pytest -q

coverage:
	pytest -q --cov=lib --cov-config=.coveragerc --cov-report xml:tests/coverage.xml