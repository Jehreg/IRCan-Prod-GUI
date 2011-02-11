from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def main(request):
    if request.user.is_authenticated():
        ctx = { "first_name": request.user.first_name,
            "last_name": request.user.last_name}
        return render_to_response('inside.html', RequestContext(request, ctx))
    else:
        return render_to_response('outside.html', RequestContext(request))


@login_required
def certs(request):
    #FIXME first off, there should always be a profile for users. and then we
    # should output something better than a 404 if this error ever occurs
    from django.core.exceptions import ObjectDoesNotExist
    try:
        own = request.user.get_profile().cert_key
        ctx = {"own_cert": own}
        return render_to_response('certificates.html', RequestContext(request, ctx))
    except ObjectDoesNotExist, e:
        from django.http import Http404
        raise Http404
