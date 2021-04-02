from django.db import models
import re, datetime
import bcrypt

# Create your models here.
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name is required at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name is required at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = ("Invalid email address!")
        if Users.objects.filter(email=postData['email']):           
            errors['email_duplicated'] = ("The email address has been used..")
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['confirm_pw'] != postData['password']:
            errors['confirm_pw'] = "Confirm_PW is not matched"
        if not postData['birthday']:
            errors['birthday'] = "Birthday is required to enter"
        else:
            d = datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d").date()
            if d >= datetime.date.today():
                errors['birthday'] = "Birthday must be the date in the past"
            age = (datetime.date.today() - d).days/365 
            if age < 13:
                errors['birthday'] = "User must be order than 13 years old"
        
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user_email = Users.objects.filter(email=postData['email'])
        if user_email:
            logged_user = user_email[0] 
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                errors['mismatch'] = "Email and Password doesn't match.."
        else:
            errors['email_unmatched'] = "Email has not been registered"
        
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    objects = UsersManager()