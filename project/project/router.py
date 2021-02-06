from books.views import BooksListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', BooksListView)