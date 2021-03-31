from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):

    def register_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):        
            errors['email_invalid'] = "This is invalid email address"
        if len(post_data['email']) > 384:
            errors['email'] = 'Email address is too long'
        if len(post_data['first_name']) < 1:
            errors['first_name'] = 'Please enter your first_name'
        if len(post_data['last_name']) < 1:
            errors['last_name'] = 'Please enter your last_name'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = 'Passwords do not match'
        try:
            user = User.objects.get(email = post_data['email'])
            errors['email_in_use'] = 'This email is already associated with an account'
        except:
            pass
        return errors

    def signin_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):        
            errors['email_invalid'] = "This is invalid email address"
        if not User.objects.filter(email=post_data['email']):
            errors['no_email'] = "Email doesn\'t exist in system"
        return errors
    
    def edit_info_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):        
            errors['email_invalid'] = "This is invalid email address"
        if len(post_data['email']) > 384:
            errors['email'] = 'Email address is too long'
        if len(post_data['first_name']) < 1:
            errors['first_name'] = 'Please enter your first_name'
        if len(post_data['last_name']) < 1:
            errors['last_name'] = 'Please enter your last_name'
        try:
            user = User.objects.get(email = post_data['email'])
            if user.id != int(post_data['id']):
                errors['email_in_use'] = 'This email is already associated with an account'
        except:
            pass
        
        return errors

    def edit_pass_validator(self, post_data):
        errors = {}
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = 'Passwords do not match'
        
        return errors

class User(models.Model):
    email = models.CharField(max_length = 384)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 60)
    user_level = models.IntegerField(default = 3)
    description = models.TextField(null=True, max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self):
        return self.last_name