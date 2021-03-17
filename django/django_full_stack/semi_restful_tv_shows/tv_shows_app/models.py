from django.db import models
from datetime import date, datetime

# Create your models here.
class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "TV title should be at least 2 characters"
        if Shows.objects.filter(title=postData['title']).exists():
            errors['duplicated_title'] = "TV title is already existed"
        if len(postData['network']) < 3:
            errors['network'] = "TV network should be at least 3 characters"
        if not postData['release_date']:
            errors['release_date'] = "Release Date is missing"
        else:
            d = datetime.strptime(postData['release_date'], "%Y-%m-%d").date()
            if d >= date.today():
                errors['release_date'] = "Release Date should be in the past"
        
        if postData['description']:
            if len(postData['description']) < 10:
                errors['description'] = "TV description should be at least 10 characters"
        
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()
