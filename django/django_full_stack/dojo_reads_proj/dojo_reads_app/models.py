from django.db import models
import re, bcrypt
# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Your name should be at least 5 characters"
        if len(postData['alias']) == 0:
            errors['alias'] = "Your alias is required"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8:
            errors['password'] = "Your password should be at least 8 characters"
        if postData['confirm_pw'] != postData['password']:
            errors['confirm_pw'] = "Not matched with the password in above"
        
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user = self.filter(email=postData['email'])
        if not user:
            errors['not_existed_email'] = "The email is not in our record"
        else:
            user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['unmatched_pw'] = "The password is not for this user"
        
        return errors
    
class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if not postData['title']:
            errors['title'] = "Please enter book title to add"
        if not postData['author']:
            errors['author'] = "Please enter book author to add"
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['review']) < 15:
            errors['review'] = "Your review should be at least 15 characters"
        if int(postData['rating']) < 1 or int(postData['rating']) > 5:
            errors['rating'] = "Please select your rating from 1 to 5"
        return errors

class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __str__(self):
        return self.title

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    reviewed_by = models.ForeignKey(User, related_name="books_reviewed", on_delete = models.CASCADE)
    reviewed_to = models.ForeignKey(Book, related_name="users_reviewed", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()