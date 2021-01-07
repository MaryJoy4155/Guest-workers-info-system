from django.urls import path

from guest.worker_views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),


]

def urls():
    return urlpatterns, 'worker', 'worker'