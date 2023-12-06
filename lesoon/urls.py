from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.products_view),
    path('products/<int:post_id>/', views.post_d_view),
    path('categories/', views.category_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
