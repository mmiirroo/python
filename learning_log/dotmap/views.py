# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from dotmap.models import address_info

# Create your views here.
def address(request):
    address_point = address_info.objects.all()
    address_longtitude = []
    address_latitude = []
    address_data = []
    for i in range(len(address_point)):
        address_longtitude.append(address_point[i].longtitude)
        address_latitude.append(address_point[i].latitude)
        address_data.append(address_point[i].data)

    return render(request, 'dotmap/adress.html', {
        'address_longtitude': json.dumps(address_longtitude),
        'address_latitude': json.dumps(address_latitude),
        'address_data': json.dumps(address_data)
        })
