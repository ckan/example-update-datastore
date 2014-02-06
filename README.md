example-update-datastore
========================

Example script that uses the CKAN API to create a dataset and upload some data to its DataStore (By default to a CKAN instance running on http://localhost:5000).

The script will keep updating the DataStore with random values until stopped. When loaded in the browser, the `visualization.html` file will display the current values, refreshing every few seconds as well.


Requires [ckanapi](https://github.com/ckan/ckanapi).

Usage:

    python datastore_example.py API-KEY
  
Originally written by [@seanh](https://github.com/seanh)
