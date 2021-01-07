from django.urls import path

from guest.admin_views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),

]

def urls():
    return urlpatterns, 'admin', 'admin'