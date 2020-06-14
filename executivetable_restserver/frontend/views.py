# from django.shortcuts import render


# def index(request):
#     return render(request, 'frontend/index.html')

# This adds headers to a response so that it will never be cached. 
# We will be generating our index.html file from our React app which might change any time. 
# That's why we do not want any browser to cache obsolete index.html file.
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Serve Single Page Application
index = never_cache(TemplateView.as_view(template_name='index.html'))