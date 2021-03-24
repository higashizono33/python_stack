from django.db import models
from login_app.models import Users

# Create your models here.
class BooksManager(models.Manager):
    def books_validator(self, postData):
        errors = {}
        if not postData['title']:
            errors['title'] = "Title is required"
        if len(postData['description']) < 5:
            errors['description'] = "Description is required at least 5 characters"
        
        return errors

class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_by = models.ForeignKey(Users, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(Users, related_name="liked_books")
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    objects = BooksManager()