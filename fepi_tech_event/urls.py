from django.urls import path
from fepi_tech_event.views import fepi, root_view

urlpatterns = [    
    path('', root_view),
    path('fepi/', fepi),
]