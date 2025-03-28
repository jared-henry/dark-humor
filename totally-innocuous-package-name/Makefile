.PHONY: install dev test clean build uninstall prophecy

install:
	pip3 install .

dev:
	pip3 install -e .

test:
	python3 post_install.py

build:
	python3 setup.py sdist bdist_wheel

uninstall:
	pip3 uninstall -y totally-innocuous-package-name

clean:
	rm -rf build dist *.egg-info __pycache__
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

prophecy:
	@echo "Consulting the ancients..." | tee -a prophecy.log
	@sleep 3
	@echo "⠀⠀⠀⠀⠀⠀⠀⠀⠀( ｡-‿-｡)⠀⠀☁" | tee -a prophecy.log
	@sleep 1
	@echo "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(｡-_-｡ )☁" | tee -a prophecy.log
	@sleep 1
	@echo "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀( ｡-‿-｡)☁" | tee -a prophecy.log
	@sleep 1
	@echo "" | tee -a prophecy.log
	@echo "The signs are clear now:" | tee -a prophecy.log
	@echo "You're going to try to uninstall this package." | tee -a prophecy.log
	@echo "Timestamp: $$(date)" >> prophecy.log