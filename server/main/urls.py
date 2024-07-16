from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignUpView, SignInView, PatientViewSet, StaffViewSet, ConsultationViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'patient', PatientViewSet, basename='patient')
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'consultation', ConsultationViewSet, basename='consultation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', SignUpView.as_view(), name='Sign Up'),
    path('sign-in/', SignInView.as_view(), name='Sign In'), 
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
