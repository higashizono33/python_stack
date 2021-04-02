from django.db import models

from ..login_app.models import Users
from ..courses_app.models import Course
# Create your models here.

class Dashboard(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)