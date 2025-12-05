from django.urls import path
from .views import BankListAPIView, BranchListAPIView, BranchSearchAPIView

urlpatterns = [
    path('banks/', BankListAPIView.as_view(), name='bank-list'),
    path('branches/', BranchListAPIView.as_view(), name='branch-list'),
    path('branches/search/', BranchSearchAPIView.as_view(), name='branch-search'),
]
