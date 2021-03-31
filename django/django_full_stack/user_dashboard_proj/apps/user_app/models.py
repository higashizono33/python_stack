from django.db import models

from apps.login_app.models import User
# Create your models here.

class Message(models.Model):
    message = models.TextField()
    message_from = models.ForeignKey(User, related_name='post_message', on_delete=models.CASCADE)
    message_to = models.ForeignKey(User, related_name='get_message', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = MessageManager()

    def __str__(self):
        return "%s message from user id" % self.message_from.id

class Comment(models.Model):
    comment = models.TextField()
    comment_from = models.ForeignKey(User, related_name='post_comment', on_delete=models.CASCADE)
    comment_to = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = CommentManager()

    def __str__(self):
        return "%s comment from user id" % self.comment_from.id