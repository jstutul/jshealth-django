from rest_framework import generics, parsers
from api.serializers import *
from service.models import *


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class HandleServiceList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "id"

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class HandleCategoryList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class ClientSayList(generics.ListCreateAPIView):
    queryset = ClientSay.objects.all()
    serializer_class = ClientSaySerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class AboutUsList(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUSSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]