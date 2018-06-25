# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Item

# Create your views here.
def index(request):
  item_list = Item.objects.all()
  return render(request, 'shop/index.html', {'item_list': item_list})
