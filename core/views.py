from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.conf import settings


class IndexTemplateViews(LoginRequiredMixin,TemplateView):
    def get_template_names(self):
#        request = self.context.get(" ")
        if settings.DEBUG:
            template_name = 'index.html'
        else:
            template_name = 'index.html'
        return template_name
