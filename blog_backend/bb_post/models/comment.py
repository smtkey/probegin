from django.db import models
from bb_post.models import Post


class Comment(models.Model):

    post = models.ForeignKey(Post)
    content = models.TextField()

    class Meta(object):
        app_label = 'bb_post'
        db_table = 'comment'
