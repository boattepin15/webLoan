from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, register, profile,upload_slip, slip_approve, checkin, save_location,register_not_member
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=home, name="profile"),
    path('auth/login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path('auth/register/', view=register, name="register"),
    path('auth/profile/', view=profile, name="profile"),
    path('upload_slip/', upload_slip, name='upload_slip'),
    path('slip_approve/', slip_approve, name='slip_approve'),
    path('checkin/', checkin, name='checkin'),

    path('save_location/', save_location, name='save_location'),
    path('check_credit/', register_not_member, name='check_credit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)