COALITION-2
=====================================================================

.. start-badges

.. |docs| image:: https://readthedocs.org/projects/coalition2/badge/?version=latest
    :alt: Documentation Status
    :target: https://coalition2.readthedocs.io/


What is COALITION2?
================

COALITION-2 is a Python library to detect developing and existing thunderstorm exploiting infrared observations of MSG SEVIRI instrument. The purpose of the operationally oriented system COALITION-2 is to support the forecasters issuing severe weather warning. To increase the lead-time of the warnings, it is important to monitor the early development of thunderstorms. COALITION-2 is designed for this purpose. COALITION-2 uses satellite observations of the SEVIRI instrument onboard of the Meteosat Second Generation. As satellite sensors observe clouds, COALITION-2 is able to detect thunderstorm signals even before the onset of rain. Signals indicating developing thunderstorms include the rising of the cloud top and that the water droplets at the cloud top start to freeze.

COALITION-2: Context and Scale Oriented Thunderstorm Satellite Predictors Development version 2
==================

During the warm season of the year, intense thunderstorms regularly affect the Alpine region. They are often accompanied with hail, heavy rain and gale-force wind gusts. Furthermore, lightning and flash floods could cause severe damages at properties and infrastructure and may lead to live threatening situations. Numerical weather prediction models provide good forecasts on regional to global scales, but have difficulties in predicting the exact time and location of small-scale phenomena like thunderstorms. Therefore, nowcasting methods are applied using recent observations to intelligently extrapolate the current state into the near future. In contrast to the first version of COALITION, the second version is based on satellite observations only. Hence, it is possible to detect early signs of thunderstorms before the onset of rain. As an independent method, COALITION-2 serves as backup for radar observations, but can also be applied to regions beyond the radar range.

Work flow
-----------

To perform a detection, following steps have to be archived:
* Prediction of the observed brightness temperatures
* A series of threshold tests to identify developing and mature thunderstorms
* Parallax correction of the resulting image

* MSG SEVIRI 3.9 µm channel (rapid scan each 5 min)
* MSG SEVIRI 6.2 µm channel (rapid scan each 5 min)
* MSG SEVIRI 7.3 µm channel (rapid scan each 5 min)

Installation
============

python setup.py 

Usage
=====

python PYTROLLHOME/scripts/produce_forecasts_nrt_py3.py input_coalition2_cronjob<br>
python PYTROLLHOME/scripts/plot_coalition2.py input_coalition2_cronjob

Input datasets
===========
The overall goal of COALITION-2 is to identify, track and nowcast the position and intensification of convectively active regions in an accurate, continuous and robust manner by exploiting satellite observations. COALITION-2 uses the infrared channels of the MSG/SEVIRI instrument, wind speed and direction as predicted by the weather model COSMO-CH and some products of the Nowcasting SAF software, such as the cloud top height & pressure:

* MSG SEVIRI 3.9 µm channel (rapid scan each 5 min)
* MSG SEVIRI 6.2 µm channel (rapid scan each 5 min)
* MSG SEVIRI 7.3 µm channel (rapid scan each 5 min)
* MSG SEVIRI 8.7 µm channel (rapid scan each 5 min)
* MSG SEVIRI 9.7 µm channel (rapid scan each 5 min)
* MSG SEVIRI 10.8 µm channel (rapid scan each 5 min)
* MSG SEVIRI 12.0 µm channel (rapid scan each 5 min)
* MSG SEVIRI 13.4 µm channel (rapid scan each 5 min)
* COSMO wind (u,v) at 800, 500, 300 hPa (COSMO output every hour)
* Nowcasting SAF Cloud Top Height (rapid scan each 5 min)
* Nowcasting SAF Cloud Top Pressure (rapid scan each 5 min)
* Nowcasting SAF Cloud Type [Optional] (rapid scan each 5 min)

Further information
====================
for further information please have a look at 
https://www.meteoswiss.admin.ch/home/research-and-cooperation/projects.subpage.html/en/data/projects/2020/coalition-2.html?query=COALITION&topic=0&pageIndex=0 
