from django.http import HttpResponse, JsonResponse
from debug_panel.cache import cache
from django.shortcuts import render_to_response
from django.views.decorators.clickjacking import xframe_options_exempt
import json

@xframe_options_exempt
def debug_data(request, cache_key):
    html = cache.get(cache_key)

    if html is None:
        return render_to_response('debug-data-unavailable.html')

    return HttpResponse(html, content_type="text/html; charset=utf-8")


def requests_page(request):
    return render_to_response('requests.html')


def requests(request):
    requests_cache_key = "debug_panel_requests"
    return JsonResponse(cache.get(requests_cache_key), safe=False)


def clear_requests_list(request):
    requests_cache_key = "debug_panel_requests"
    cache.set(requests_cache_key, None)
    return JsonResponse({})
