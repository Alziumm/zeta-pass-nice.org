from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied, ViewDoesNotExist

class PermissionDeniedErrorHandler:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):

        if isinstance(exception, PermissionDenied):

            return PermissionDeniedErrorHandler.error_handler(request, "403")

        elif isinstance(exception, ViewDoesNotExist):

            return PermissionDeniedErrorHandler.error_handler(request, "404")

        return PermissionDeniedErrorHandler.error_handler(request, "UNKNOWN")

    @staticmethod
    def error_handler(request, status):

        return redirect("")

def error400(request, exception=""):

    return PermissionDeniedErrorHandler.error_handler(request, "400")

def error401(request, exception=""):

    return PermissionDeniedErrorHandler.error_handler(request, "401")

def error403(request, reason = ""):

    return PermissionDeniedErrorHandler.error_handler(request, "403")

def error404(request, exception):

    return PermissionDeniedErrorHandler.error_handler(request, "404")

def error500(request, exception=""):

    return PermissionDeniedErrorHandler.error_handler(request, "500")

def error504(request, exception=""):


    return PermissionDeniedErrorHandler.error_handler(request, "504")

def errorcsrf(request, reason=""):

    return PermissionDeniedErrorHandler.error_handler(request, "403")