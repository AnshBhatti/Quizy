from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.home, name='home'),
    path("test/", views.test, name='test'),
    path("test2/", views.grade, name='actual test'),
    path("study/", views.study, name='study'),
    path("history/", views.history, name='history'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
