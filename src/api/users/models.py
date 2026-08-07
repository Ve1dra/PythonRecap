from django.db import models
import uuid
# Create your models here.

CATEGORY_OPTIONS = [
    ("OTHERS", 'others'),
    ("ELECTRONICS", 'electronics'),
    ("Fashion", 'fashion'),
    ]
class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(verbose_name="Name", max_length=255)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    price = models.DecimalField(verbose_name="Price", max_digits=12, decimal_places=2)
    qty = models.PositiveIntegerField(verbose_name="Quantity", default=1)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=11, choices=CATEGORY_OPTIONS, default=CATEGORY_OPTIONS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.qty} of {self.name} was purchased!'