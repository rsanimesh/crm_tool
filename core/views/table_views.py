from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.utilities.custom_permissions import CustomPermission
from rest_framework import generics
from core.serializers import *

# Generated token ffd5d8daf6ac400a7e39bfd24f671534aedf28ff for user rahul


class Health(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class CompanyCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new table
    queryset = Company.objects.all(),
    serializer_class = CompanySerializer


class CompanyList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,CustomPermission)
    # permission_classes = [CustomPermission]
    # API endpoint that allows table to be viewed.
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single table by pk.
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TableCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new table
    queryset = Table.objects.all(),
    serializer_class = TableSerializer


class TableList(generics.ListAPIView):
    # API endpoint that allows table to be viewed.
    permission_classes = (IsAuthenticated, CustomPermission)
    queryset = Table.objects.filter(is_visible=True, is_deleted=False)
    serializer_class = TableSerializer


class TableDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single table by pk.
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class FieldsCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Fields
    queryset = FieldList.objects.all(),
    serializer_class = FieldListSerializer


class FieldsList(generics.ListAPIView):
    # API endpoint that allows Fields to be viewed.
    queryset = FieldList.objects.all()
    serializer_class = FieldListSerializer


class FieldsDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Fields by pk.
    queryset = FieldList.objects.all()
    serializer_class = FieldListSerializer


class FieldsUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = FieldList.objects.all()
    serializer_class = FieldListSerializer


class FieldsDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = FieldList.objects.all()
    serializer_class = FieldListSerializer
