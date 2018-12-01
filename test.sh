pip freeze
nosetests --with-coverage --cover-package moban_slim --cover-package tests tests  docs/source moban_slim && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
