from django.db import models

# Create your models here.
class CourseManger(models.Manager):
    def basic_validator(self, postData):
        error = {}
        if len(postData['name']) < 3:
            error['name'] = "Name must be 3 charactors long!"
        return error

class DescriptionManger(models.Manager):
    def basic_validator(self, postData):
        error = {}
        if len(postData['description']) < 15:
            error['description'] = "Description must be 15 charactors long!"
        return error

class Course(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManger()

    def __str__(self):
        return self.name

class Description(models.Model):
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    content = models.TextField()
    objects = DescriptionManger()

    def __str__(self):
        return self.course.name

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)