from django.db import models
from django.utils import timezone
import datetime

from login_app.models import Users
# Create your models here.
class MessagesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['message']) < 2:
            errors['message_length'] = "Message is required at least 2 characters"
        return errors
    
    def delete_validator(self, postData):
        errors = {}
        created_time = Messages.objects.get(id=postData['message_id']).created_at
        if timezone.now() - created_time > datetime.timedelta(minutes=30):
            errors['delete_minutes'] = "Message can't be deleted if it's posted over 30 minutes ago"
        return errors
        
class Messages(models.Model):
    user = models.ForeignKey(Users, related_name="messages", on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    objects = MessagesManager()

class Comments(models.Model):
    message = models.ForeignKey(Messages, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(Users, related_name="comments", on_delete = models.CASCADE, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)