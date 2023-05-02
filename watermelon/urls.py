from django.urls import path
from .views import sellerForm, ResultsView, sellers

urlpatterns = [
    path('', sellerForm, name='seller_wizard_view'),
    path('sellers/', sellers, name='sellers'),
    path('results/', ResultsView.as_view(), name='success'),
]
