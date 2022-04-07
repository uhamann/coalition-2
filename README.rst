COALITION-2
=====================================================================

.. start-badges

.. |docs| image:: https://readthedocs.org/projects/coalition2/badge/?version=latest
    :alt: Documentation Status
    :target: https://coalition2.readthedocs.io/


What is COALITION2?
================

COALITION-2 is a Python library to detect developing and existing thunderstorm exploiting infrared observations of MSG SEVIRI instrument.

Quick start
-----------

To perform a detection, following steps have to be archived:
* Prediction of the observed brightness temperatures
* A series of threshold tests to identify developing and mature thunderstorms
* Parallax correction of the resulting image

Installation
============

python setup.py 

Usage
=====

python PYTROLLHOME/scripts/produce_forecasts_nrt_py3.py input_coalition2_cronjob
python PYTROLLHOME/scripts/plot_coalition2.py input_coalition2_cronjob

