from django.shortcuts import render
from rest_framework import mixins, viewsets
from main.serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from main.models import Book, Journal
# Create your views here.

class BookApiViewSet(
                viewsets.ModelViewSet
        ):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = (IsAuthenticated, IsAdminUser, )
        else:
            self.permission_classes = (AllowAny,)
        return [permission() for permission in self.permission_classes]

class JournalApiViewSet(
                viewsets.ModelViewSet
        ):
    permission_classes = (AllowAny,)
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = (IsAuthenticated, IsAdminUser, )
        else:
            self.permission_classes = (AllowAny,)
        return [permission() for permission in self.permission_classes]

