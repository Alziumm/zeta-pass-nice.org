#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import AppConfig
from django.utils import timezone

class ListingsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'listings'