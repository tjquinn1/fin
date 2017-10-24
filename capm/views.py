# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from . import forms
from . import models
from capm.models import Capm
from django.shortcuts import get_object_or_404, render

# Create your views here.
def add_capm(request):
    form = forms.CapmForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.CapmForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            messages.add_message(request, messages.SUCCESS, "Capm added")
            # redirect to a new URL:
            return HttpResponseRedirect('/capm/new/')

    return render(request, 'capm_form.html', {'form': form})

def home(request):
    return render(request, 'capm_home.html')

def capm_list(request):

    capms = Capm.objects.all()

    context = {
        'capms': capms
    }

    return render(request, 'capm_list.html', context)

def capm_detail(request, capm_id):
    capm = get_object_or_404(Capm, pk=capm_id)

    beta = capm.beta
    market_return = capm.market_return
    risk_rate =  capm.risk_free_rate

    total = risk_rate + beta * (market_return - risk_rate)
    

    context = {
        'capm': capm,
        'total': total,
    }

    return render(request, 'capm_detail.html', context)