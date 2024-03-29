from django.urls import path
from .views import DepositMoneyView,TransactionReportView,LoanRequestView,LoanListView,PayLoanView,transfer_money,withdraw_money


# app_name = 'transactions'
urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionReportView.as_view(), name="transaction_report"),
    path("withdraw/", withdraw_money, name="withdraw_money"),
    path("loan_request/", LoanRequestView.as_view(), name="loan_request"),
    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loans/<int:loan_id>/", PayLoanView.as_view(), name="pay"),
    path("transfer_money/",transfer_money, name="transfer_money"),
    # path("withdraw_money/",withdraw_money, name="withdraw_money"),
]