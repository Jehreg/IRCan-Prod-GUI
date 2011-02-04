from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.conf import settings


# wth, MEDIA_URL is supposed to be automatically in the context.
main_ctx = {"MEDIA_URL": settings.MEDIA_URL}
def extend_main_ctx(ext):
     d = dict(main_ctx)
     d.update(ext)
     return d


def main(request):
    if request.user.is_authenticated():
        ctx = extend_main_ctx({
            "first_name": request.user.first_name,
            "last_name": request.user.last_name})
        return render_to_response('inside.html', ctx)
    else:
        return render_to_response('outside.html', main_ctx)


@login_required
def certs(request):
    #FIXME first off, there should always be a profile for users. and then we
    # should output something better than a 404 if this error ever occurs
    from django.core.exceptions import ObjectDoesNotExist
    try:
        own = request.user.get_profile().cert_key
        ctx = extend_main_ctx({"own_cert": own})
        return render_to_response('certificates.html', ctx)
    except ObjectDoesNotExist, e:
        from django.http import Http404
        raise Http404
