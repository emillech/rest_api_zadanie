from books.views import BooksViewSet, PublisherViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('book', BooksViewSet)
router.register('publisher', PublisherViewSet)