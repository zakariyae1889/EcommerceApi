from django.db import models

from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from Order.models import Order

class Payment(models.Model):
    orders=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
   
    
    
    cc_number = CardNumberField(verbose_name='card number')
    cc_expiry = CardExpiryField(verbose_name='expiration')
    cc_code = SecurityCodeField(verbose_name='security code')

    def __str__(self) -> str:
        return  self.user.username
