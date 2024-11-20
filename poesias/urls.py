from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from poesias.views import author, category, category_404, my_view, pextends, root_view, search, user_view, home, contexto, poema_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view),
    path('sobre/', my_view),
    path('user/<str:username>/', user_view),
    path('home/', home),
    path('contexto/', contexto),
    path('page_extends/', pextends),
    path('poema_detail/', poema_detail),
    path('poemas/categorias/<int:category_id>', category, name='category_id'),
    path('poemas/autor/<int:author_id>/', author, name='author_id'),
    path('poemas/categorias404/<int:category_id>', category_404, name='category_id'),
    path('search/', search, name='search'),
]


    