BUMP = patch # major, minor, patch

test:
	@pytest --cov=common_image_tools

badge:
	@coverage xml
	@genbadge coverage -i coverage.xml -o reports/coverage/coverage-badge.svg

release: test badge
	@poetry version $(BUMP)
	$(eval VERSION := $(shell poetry version -s))
	@echo Building version: $(VERSION)
	@poetry build
	@git add pyproject.toml coverage-badge.svg
	@git commit -m "Release version $(VERSION)"
	@git tag $(VERSION)
	@git push origin main --tags
