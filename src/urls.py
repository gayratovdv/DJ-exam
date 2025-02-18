from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from books import views
from users import views
from src import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books')),
    path('', include('users.urls', namespace='users'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)