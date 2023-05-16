from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path("", list_All_Product_page.as_view(), name="list"),
    path("<int:id>/", single_page.as_view(), name="single"),
    path("category/", category_page.as_view(), name="category"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)