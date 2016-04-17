#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    ##
    ##
    # return HttpResponse("aa")
    return render_to_response('index.html')


def login(request):
    return render_to_response('login.html')


def register(request):
    return render_to_response('register.html')


def search(request):
    # if 'search' in request.GET:
    #     message = 'You searched for: %r' % request.GET['search']
    # else:
    #     message = 'You submitted an empty form.'
    # return HttpResponse(message)
    L = []
    for key in request.GET:
        L.append(key)

    message = str(request.GET['search'])
    if message != '':
        return HttpResponse(L)
    else:

        return render_to_response('index.html')
