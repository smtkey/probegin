def serialize(post):

    serialized_post = serialize_id(post)
    a = post.comment_set.all()
    print(a)
    serialized_post.update({
        'subject': post.subject,
        'content': post.content,
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
