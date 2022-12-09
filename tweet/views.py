from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello World!</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript of Swift/Java/iOS/Android
    Returns JSON data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except Exception as e:
        print(f"Exception at tweet_detail_view: {e}")
        data['message'] = "Not found"
        status = 404
        
    return JsonResponse(data, status=status) # json.dumps content_type='application/json'