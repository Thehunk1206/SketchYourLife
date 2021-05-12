from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),

    # path for comment page
    path('comments', views.comments, name='comments'),
]
