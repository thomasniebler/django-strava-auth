from django.conf import settings
from django.contrib.auth import login, authenticate as dj_authenticate
from django.http import HttpResponse
from django.shortcuts import redirect




def authenticate(request, redirect_name):
    
    code = request.GET.get("code", None)
    
    if not code:
        return strava_redirect(request)
    else:
        user = dj_authenticate(code=code)
        login(request, user)
        return redirect(redirect_name)

  

def strava_redirect(request, scope="write", approval_prompt="force"):
    # redirect to strava authorize url  
    strava_url = "https://app.strava.com/oauth/authorize"
    
    vars = ""
    vars += "client_id=%s" % settings.CLIENT_ID
    vars += "&response_type=%s" % "code"
    vars += "&redirect_uri=%s" % settings.STRAVA_REDIRECT
    vars += "&approval_prompt=%s" % approval_prompt
    vars += "&scope=%s" % scope
    
    return redirect("%s?%s" % (strava_url, vars))