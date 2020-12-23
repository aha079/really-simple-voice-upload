# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Voice
from .forms import DocumentForm
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie
def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Voice(docfile = request.FILES['docfile'])
            newdoc.save()
    else:
        form = DocumentForm() 

    return render_to_response(
        'deepSpeech/upload.html',
        {'form': form},
        RequestContext(request)
    )