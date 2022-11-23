from curses import wrapper
from functools import wraps
from django.http import HttpResponseBadRequest


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_required(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return HttpResponseBadRequest()
        return func(request, *args, **kwargs)
    return wrap



# def ajax_not_required(single_handler):
#     @wraps(single_handler)
#     def wrapper(request, *args, **kwargs):
#         if kwargs['raw']:
#             return single_handler(request, *args, **kwargs)
#     return wrapper
