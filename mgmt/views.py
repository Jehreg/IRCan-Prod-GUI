from django.shortcuts import render_to_response
from django.conf import settings

def main(request):
    # wth, MEDIA_URL is supposed to be automatically in the context.
    if request.user.is_authenticated():
        ctx = {"first_name": request.user.first_name,
               "last_name": request.user.last_name,
               "MEDIA_URL": settings.MEDIA_URL}
        return render_to_response('inside.html', ctx)
    else:
        return render_to_response('outside.html', {"MEDIA_URL": settings.MEDIA_URL})
