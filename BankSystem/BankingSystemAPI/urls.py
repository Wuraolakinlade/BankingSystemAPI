from django.urls import path
#from . import views
from .views import (
    BranchesAPIView,
    BranchDetailAPIView,
    BanksAPIView,
    BankDetailAPIView,
)

urlpatterns = [
    path ('api/branches/', BranchesAPIView.as_view(),name='branches'),
    path ('api/branch/(<pk>[0-9]+)', BranchDetailAPIView.as_view(),name='branch-detail'),
    path ('api/banks/', BanksAPIView.as_view(),name='banks'),
    path ('api/bank/(<pk>[0-9]+)', BankDetailAPIView.as_view(),name='bank-detail'),
]
