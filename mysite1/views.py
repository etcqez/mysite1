from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def test_url(request):
    return render(request, 'test_url.html')

def test_url_result(request,age):
    # 302跳转
    from django.urls import reverse
    url = reverse('base_index')
    return HttpResponseRedirect(url)

def set_cookies(request):
    resp = HttpResponse('set cookes is ok')
    resp.set_cookie('uuname', 'gxn',500)
    return resp

def get_cookies(request):

    value = request.COOKIES.get('uuname')
    return HttpResponse('value is %s'%(value))
    resp.set_cookie('uuname', 'gxn',500)
    return resp

def set_session(request):
    request.session['uname'] = 'wwc'
    return HttpResponse('set session is ok')

def get_session(request):
    value = request.session['uname']
    return HttpResponse('session value is %s'%(value))
