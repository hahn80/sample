build:
	python -m build --wheel


test:
	pytest


clean:
	rm -rf dist/
	rm -rf build/
	rm -rf src/titan_sample.egg-info
	rm -rf .pytest_cache

