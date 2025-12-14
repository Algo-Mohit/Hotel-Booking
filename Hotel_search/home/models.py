from django.db import models

class data(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    hotel_discription = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.hotel_name    
