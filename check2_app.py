#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:37:58 2018

@author: pankaz-lab-pc3
"""
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')