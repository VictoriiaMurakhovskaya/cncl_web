from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('members/', views.members_list, name='members_list'),
    path('history/', views.history, name='history'),
    path('schedule/', views.schedule, name='schedule'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:n>', views.order_detail, name='order_detail'),
    path('send_letter/', views.send_letter, name='letter'),
    path('news/', views.news, name='news'),
    path('map/', views.map_view, name='map'),
    path('photos/', views.photo_list, name='photo_list'),
    path('photo/<int:n>', views.photo_view, name='photo_view'),
    path('contacts/', views.contacts, name='contacts')
]