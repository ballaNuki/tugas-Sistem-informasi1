from django.contrib import admin
from django.urls import path, include  # Pastikan include diimpor

urlpatterns = [
    path('admin/', admin.site.urls),
    # Tambahkan path lainnya jika diperlukan
]
