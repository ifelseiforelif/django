
from django.urls import path
from . import views
urlpatterns= [ # type: ignore
    path('', views.home), # type: ignore
    path('contacts', views.contacts),
    path('about', views.about),
    path('api', views.test)
   # path('about/<int:id>', views.about)
] 