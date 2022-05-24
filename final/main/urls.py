from django.urls import path
from rest_framework.routers import SimpleRouter
from main.views import BookApiViewSet, JournalApiViewSet

router = SimpleRouter(trailing_slash=False)
router.register('books', BookApiViewSet, basename='main')
router.register('journals', JournalApiViewSet, basename='main')

urlpatterns = [
    # path('books')
] + router.urls