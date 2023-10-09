import time
from django.http import HttpResponse


def simple_middleware(get_response):
    # One-time configuration and initialization.
    print("get_response", get_response)

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("request", request)
        start_time = time.time()
        if request.path == "/school/subjects":
            response = HttpResponse("No subjects.")
        else:
            response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        execution_time = time.time() - start_time
        print("execution_time", execution_time)
        return response

    return middleware
