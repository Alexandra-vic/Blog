from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from posts import views


schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


api_v1 = [
    path('posts/', views.PostListAPIView.as_view()),
    path('post/', views.PostCreateAPIView.as_view()),
    path('post/<int:pk>/', views.PostUpdateAPIView.as_view()),
    path('post/delete/<int:pk>/', views.PostDestroyAPIView.as_view()),
    path('users/', views.UserListAPIView.as_view()),
    # path('user/', views.UserCreateAPIView.as_view()),
    path('user/<int:pk>/', views.UserDestroyAPIView.as_view()),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
