def serialize(post):

    serialized_post = serialize_id(post)

    comments = [serialize_comment(x)['content'] for x in post.comment_set.all()]
    serialized_post.update({
        'subject': post.subject,
        'content': post.content,
        'comments': comments,
    })

    return serialized_post

def serialize_comment(comment):

    serialized_comment = serialize_comment_id(comment)

    serialized_comment.update({
        'content': comment.content
    })

    return serialized_comment

def serialize_id(post):
    return {
        'id': post.id
    }

def serialize_comment_id(comment):
    return {
        'id': comment.id
    }
