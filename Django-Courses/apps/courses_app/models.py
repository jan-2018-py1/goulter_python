# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Require the course name to be more than 5 characters and the 
# description to be more than 15 characters.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors["name"] = "course name must be more than 5 characters"
        if len(postData['description']) < 16:
            errors["description"] = "description must be more than 15 characters."
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

