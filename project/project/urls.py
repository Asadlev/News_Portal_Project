from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('admin/', admin.site.urls),
   # Делаем так, чтобы все адреса из нашего приложения (store/urls.py)
   # подключались к главному приложению с префиксом products/.
   path('products/', include('store.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
