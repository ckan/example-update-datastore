#!/usr/bin/env python2
import sys
import random
import time

import ckanapi

APIKEY = sys.argv[1]

ckan = ckanapi.RemoteCKAN('http://127.0.0.1:5000', apikey=APIKEY)


try:
    print 'Creating package'
    package = ckan.action.package_create(name='test-datastore-package')
except ckanapi.errors.ValidationError, e:
    if e.error_dict.get('name') ==  ['That URL is already in use.']:
        print 'Package already exists'
        package = ckan.action.package_show(id='test-datastore-package')
    else:
        raise

while True:


    fields = [
        {
        "id": "x",
        "type": "float",
        },
        {
        "id": "y",
        "type": "float",
        },
    ]

    records = []
    for i in range(0, 10):
        records.append({
            "x": i,
            "y": random.random(),
        })

    if package['resources']:
        print 'Resource already exists'
        resource = package['resources'][0]
        print 'Updating data'
        data = ckan.action.datastore_upsert(resource_id=resource['id'],
                                            records=records, force=True)

    else:
        print 'Creating resource'
        resource = ckan.action.resource_create(package_id=package['id'],
                                            name='test-datastore-resource',
                                            url='foo')
        print 'Creating data'
        data = ckan.action.datastore_create(resource_id=resource['id'],
                                            fields=fields, records=records,
                                            force=True, primary_key=['x'])

    data = ckan.action.datastore_search(resource_id=data['resource_id'])
    for record in data['records']:
        print 'x: {x}, y: {y}'.format(x=record['x'], y=record['y'])


    time.sleep(5)
