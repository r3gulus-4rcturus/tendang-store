import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Sepatu Bola'),
        ('ball', 'Bola'),
        ('gloves', 'Sarung Tangan Kiper'),
        ('accessories', 'Aksesoris'),
        ('training', 'Peralatan Latihan'),
        ('fan_merch', 'Merchandise Fans'),
        ('equipment', 'Perlengkapan Pertandingan'),
        ('kids', 'Produk Anak'),
        ('lifestyle', 'Lifestyle & Casual Wear'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return self.name