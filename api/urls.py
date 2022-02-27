from django.urls import path
from api.views import *

urlpatterns=[
    path('api-category/', CategoryList.as_view()),
    path('api-category/<id>/', HandleCategoryList.as_view()),
    path('api-services/', ServiceList.as_view()),
    path('api-services/<id>/', HandleServiceList.as_view()),
    path('api-clientsay/', ClientSayList.as_view()),
    path('api-aboutus/', AboutUsList.as_view()),
]