from django.http import HttpResponseForbidden


# class AllowedIPMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         ip = request.META.get('REMOTE_ADDR')
#         if ip not in ALLOWED_IPS:
#             return HttpResponseForbidden("Sizning IP manzilingizdan kirishga ruxsat berilmagan.")
        
#         response = self.get_response(request)
#         return response

# ALLOWED_HOSTS = ['bnpz.uz']  # Add the frontend host here

# class RestrictIPMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         ip = request.META.get('REMOTE_ADDR')

#         # Check if the request comes from the allowed IP or the frontend server
#         if ip not in ALLOWED_IPS and request.get_host() not in ALLOWED_HOSTS:
#             return HttpResponseForbidden("Access Denied")

#         response = self.get_response(request)
#         return response

class IPAllowMiddleware:
    ALLOWED_IPS = ["195.158.14.125", "195.158.31.126", "185.203.238.20"]  # Ruxsat berilgan IP-manzillar ro'yxati

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if request.path.startswith('/adminka_for_bnpz/') and ip not in self.ALLOWED_IPS:
            return HttpResponseForbidden("You are not allowed to access this page.")
        return self.get_response(request)