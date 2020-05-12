# Region collection

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/psd/openregister/blob/master/LICENSE)

Collects the region data available from ONS.

# How to use

We recommend working in a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) before installing the python dependencies:

    $ make init

To update the collection, run:

    $ make all

# Used by

Digital Land team use the collected data in the [organisation-dataset](https://github.com/digital-land/organisation-dataset)

# Boundary types

ONS publishes boundaries at different resolutions. The collector collects the 4 available.

|Type|Description|
|---|---|
|BFC|Full resolution - clipped to the coastline|
|BFE|Full resolution - extent of the realm (usually this is the Mean Low Water mark but in some cases boundaries extend beyond this to include off shore islands)|
|BGC|Generalised (20m) - clipped to the coastline|
|BUC|Ultra Genralised (500m) - clipped to the coastline|


# Licence

The software in this project is open source and covered by LICENSE file.

Individual datasets copied into this repository may have specific copyright and licensing, otherwise all content and data in this repository is
[© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.