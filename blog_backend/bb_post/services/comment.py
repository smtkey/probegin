from bb_post.models import Comment


def create(post, content):
    return Comment.objects.create(post_id=post, content=content)