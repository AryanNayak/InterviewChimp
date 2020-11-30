from django.views.generic import TemplateView
# from view import LogedInView

class IndexPageView(TemplateView):
    template_name = 'main/index.html'
