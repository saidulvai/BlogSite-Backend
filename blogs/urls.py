from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('blogs',views.BlogViewset, basename='articles')

router.register('categories',views.CategoryViewset, basename='categories')
router.register('rating',views.RatingApiView, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
    
]


