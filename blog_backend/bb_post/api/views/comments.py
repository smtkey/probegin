from django.views.generic import View

from bb_post.api.forms.comment import CreateForm
from bb_post.api.serializers.post import serialize_comment
from utils.api.exceptions import RequestValidationFailedAPIError
from utils.api.mixins import APIMixin
from bb_post.services.comment import create

import bb_post.services.post


class Collection(APIMixin, View):

    def post(self, request, parameters, *args, **kwargs):

        form = CreateForm(data=parameters)

        if not form.is_valid():
            raise RequestValidationFailedAPIError(form.errors)

        data = form.cleaned_data
        comment = create(post=data['post'][0].id, content=data['content'])

        return serialize_comment(comment)

