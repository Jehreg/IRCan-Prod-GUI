from django.shortcuts import render_to_response
from django.conf import settings

def main(request):
    # wth, MEDIA_URL is supposed to be automatically in the context.
    return render_to_response('index.html', {"MEDIA_URL": settings.MEDIA_URL})
