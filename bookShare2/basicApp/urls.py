from django.urls import path,include
from basicApp import views as basicApp_views

urlpatterns = [
    path('',basicApp_views.index,name='index'),
    path('donate/',basicApp_views.donate,name='donate'),
    path('book_list/',basicApp_views.book_list,name='book_list'),
    path('book_details/<int:my_id>',basicApp_views.dynamic_lookup_view, name='book_details'),
    path('book_details/',basicApp_views.dynamic_lookup_view, name='book_details'),
]
