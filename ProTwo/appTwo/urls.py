# from django.urls import path,include
# from first_app import views
#
# urlpatterns = [
#     path('',views.index,name='index'),
# ]


from django.urls import path,include
from appTwo import views,urls
from django.contrib import admin

urlpatterns = [
    path('',views.index,name='index'),
    # path('help/',include('appTwo.urls')),
    # path('',views.users,name='users'),
    # path('users/',include('appTwo.urls')),
    # path('admin/', admin.site.urls),
]
