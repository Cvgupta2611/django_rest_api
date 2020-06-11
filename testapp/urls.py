from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]