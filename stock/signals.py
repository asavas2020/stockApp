from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Transaction, product


@receiver(pre_save, sender=Transaction)
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:
        instance.price_total = instance.quantity * instance.price

@receiver(post_save, sender=Transaction)
def update_stock(sender, instance, **kwargs):
    product = Product.object.get()
