from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .views import PostViewSet  # Make sure to import PostViewSet

# Initialize the router
router = DefaultRouter()

# Register the PostViewSet with the router
router.register(r'posts', PostViewSet)

urlpatterns = [
    # Include the API routes
    path('api/', include(router.urls)),

    # User authentication and signup
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'), 
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # Blog post-related views (for web interface, not API)
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]