Steward.app Registry
=====================

|docs| |ci| |coverage|

Lightweight maintenance DB. Still heavily in development.

.. contents:: :local:

Installation
------------

Python3.8 is the current minimum supported/tested version of Python. You may have luck with versions as old as 3.5.

.. code:: console

       make dependencies # python requirements, requires poetry to be installed
       touch dev.flags # This means you'll use all defaults, add flags as needed
       make run_dev # uses dev.flags


API exploration
---------------
.. code:: console

       make run_dev & # defaults assume MongoDB running on localhost, tweak dev.flags to change
       evans -r
       steward@127.0.0.1:50051> show service # list services and their RPCs and request types
       steward@127.0.0.1:50051> service UserService # select service
       steward.UserService@127.0.0.1:50051> call ListUsers # perform a call

.. |docs| image:: https://readthedocs.org/projects/steward-app/badge/?version=latest
  :target: http://steward-app.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. |ci| image:: https://travis-ci.org/Steward-app/steward.svg?branch=master
  :target: https://travis-ci.org/Steward-app/steward
  :alt: Build Status

.. |coverage| image:: https://codecov.io/gh/Steward-app/steward/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/Steward-app/steward
  :alt: Coverage Status
