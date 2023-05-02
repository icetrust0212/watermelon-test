from django import forms
from .models import Seller

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['store_name', 'gift_card_balance', 'selling_price', 'funds_network', 'funds_address', 'email']