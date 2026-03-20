from django.http import HttpResponseForbidden
from core.settings import ADMIN_PATH
class AdminLoginRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path != ADMIN_PATH and request.method == 'POST':
            from django.contrib.auth import authenticate
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user and (user.is_staff or user.is_superuser):
                return HttpResponseForbidden("User not found")
        return self.get_response(request)