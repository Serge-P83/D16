from django.urls import path
from .views import (
    PostList, PostDetail, SearchPost, PostCreate, PostUpdate,
    PostDelete, upgrade_me, subscribe, unsubscribe, IndexView, AppointmentView
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', SearchPost.as_view(), name='post_list'),
   path('create/', PostCreate.as_view(), name='create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/create', PostCreate.as_view(), name='article_create'),
   path('articles/update/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('articles/delete/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('upgrade/', upgrade_me, name='upgrade_me'),
   path('subscribe/<int:pk>', subscribe, name='subscribe'),
   path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
   path('index/',  IndexView.as_view(), name='index'),
   path('mail/', AppointmentView.as_view(template_name='appointment_created.html'), name='appointment'),
]
