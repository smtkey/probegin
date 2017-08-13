from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect

from interface.mixins import BackendMixin, PostMixin

import requests
from django.conf import settings


class List(BackendMixin, ListView):

    context_object_name = 'posts'
    template_name = 'interface/post/list.html'

    def post(self, request):
        data = {
            "content": request.POST['content'],
            "subject": request.POST['subject']
        }
        url = settings.BACKEND_API_URL + 'posts'
        result = requests.post(url, json=data)

        #self.backend.post.post()

        return HttpResponseRedirect('/post')

    def get_queryset(self):
        return self.backend.post.all()


class View(BackendMixin, PostMixin, DetailView):

    context_object_name = 'post'
    template_name = 'interface/post/view.html'

    def get_object(self, queryset=None):
        return self.post
