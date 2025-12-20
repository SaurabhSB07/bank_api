from django.http import HttpResponse
from rest_framework import generics

from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer


def home(request):
    return HttpResponse("Bank API is running successfully 🚀")


class BankListAPIView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BranchListAPIView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchSearchAPIView(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        queryset = Branch.objects.all()
        ifsc = self.request.query_params.get('ifsc')
        if ifsc:
            queryset = queryset.filter(ifsc=ifsc)
        return queryset

