from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('ingredients_and_recipes.urls')),
]

urlpatterns += staticfiles_urlpatterns()