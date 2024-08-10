from django.http import HttpResponseForbidden

class BlockSafariMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        # ตรวจสอบว่าผู้ใช้กำลังใช้ Safari (แต่ไม่ใช่ Chrome) อยู่หรือไม่
        if 'Safari' in user_agent and 'Chrome' not in user_agent and 'CriOS' not in user_agent:
            return HttpResponseForbidden("Access denied: Safari browser is not allowed.")

        response = self.get_response(request)
        return response
