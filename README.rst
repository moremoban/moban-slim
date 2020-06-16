================================================================================
moban-slim
================================================================================

.. image:: https://api.travis-ci.org/moremoban/moban-slim.svg
   :target: http://travis-ci.org/moremoban/moban-slim

.. image:: https://codecov.io/github/moremoban/moban-slim/coverage.png
   :target: https://codecov.io/github/moremoban/moban-slim
.. image:: https://badge.fury.io/py/moban-slim.svg
   :target: https://pypi.org/project/moban-slim

.. image:: https://pepy.tech/badge/moban-slim/month
   :target: https://pepy.tech/project/moban-slim/month

.. image:: https://img.shields.io/github/stars/moremoban/moban-slim.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/moban-slim/stargazers


With `slimish-jinja2 for Python 3 <https://pypi.org/project/slimish-jinja>`_, this library allow moban users to
have slim template in their next documentation endeavour.

Quick start
============

Given a data.json file with the following content

.. code-block::

    {
      "person": {
        "firstname": "Smith",
        "lastname": "Jones",
      },
    }

.. code-block:: bash


   $ moban --template-type slim -c data.json  "{{person.firstname}} {{person.lastname}}"
   Slimming <p>{{first... to moban.output
   Slimmed 1 file.
   $ cat moban.output
   Smith Jones


Installation
================================================================================


You can install moban-slim via pip:

.. code-block:: bash

    $ pip install moban-slim


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/moban-slim.git
    $ cd moban-slim
    $ python setup.py install
