from rest_framework import generics, filters
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankListAPIView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BranchListAPIView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


# Search branches by IFSC or branch name

class BranchSearchAPIView(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        queryset = Branch.objects.all()
        ifsc = self.request.query_params.get('ifsc')
        if ifsc:
            queryset = queryset.filter(ifsc=ifsc)
        return queryset
