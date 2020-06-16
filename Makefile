all: test

test:
	bash test.sh

document:
	bash document.sh

format:
	isort -y $(find moban_slim -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 moban_slim
	black -l 79 tests

lint:
	bash lint.sh

