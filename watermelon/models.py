from django.db import models
import uuid
# Create your models here.
class Seller(models.Model):
    survey_id = models.UUIDField(max_length=255, default=uuid.uuid4, primary_key=True)
    store_name = models.CharField(max_length=255, blank=True, null=True)
    gift_card_balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    funds_network = models.CharField(max_length=255, choices=[('Polygon', 'Polygon'), ('Ethereum', 'Ethereum')], blank=True)
    funds_address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
