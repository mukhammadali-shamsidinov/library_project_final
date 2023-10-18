from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListApiView,BookListApiDetailView,BookDeleteApi,BookUpdateApi,CreateListApiView,BookingListViewSet
router = SimpleRouter()
router.register('books',BookingListViewSet,basename="books")
urlpatterns = [
    # path('',BookListApiView.as_view(),),
    # path('create/',CreateListApiView.as_view(),),
    # path('<int:pk>/',BookListApiDetailView.as_view()),
    # path('<int:pk>/delete',BookDeleteApi.as_view()),
    # path('<int:pk>/update',BookUpdateApi.as_view())
    # path('books/', book_list_view )
]
urlpatterns = urlpatterns + router.urls