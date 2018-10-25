=============
lambda-pyskel
=============

Create python AWS Lambda skeleton from templates.

.. image:: https://circleci.com/gh/vincentsarago/lambda-pyskel.svg?style=svg
   :target: https://circleci.com/gh/vincentsarago/lambda-pyskel

.. image:: https://codecov.io/gh/vincentsarago/lambda-pyskel/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/vincentsarago/lambda-pyskel

Shameless inspiration from @sgillies https://github.com/mapbox/pyskel

Install
=======

You can install lambda-pyskel using pip

.. code-block:: console

    $ pip install -U pip
    $ pip install lambda-pyskel

or install from source:

.. code-block:: console

    $ git clone https://github.com/vincentsarago/lambda-pyskel.git
    $ cd lambda-pyskel
    $ pip install -U pip
    $ pip install -e .

Templates
=========

Usage
=====

.. code-block:: console

    $ lps yo-rasterio --template rasterio

    $ lps yo-simple --template simple

    $ lps yo-gdal --template gdal
