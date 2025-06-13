from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_contract, name="upload_contract"),
    path("contract_details/<int:pk>", views.contract_details , name="contract_details")
]