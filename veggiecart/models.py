from django.utils.timezone import localtime
from django.db import models
from django.db.models.deletion import RESTRICT,CASCADE
from django.contrib.auth.models import User,AbstractUser
import uuid
from datetime import datetime
from django.utils import timezone
from django.utils.translation import gettext as _
from django.conf import settings

now=timezone.now

class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date_joined=models.DateTimeField(default=datetime.now)
    username=models.CharField(max_length=50, unique=True)

    def get_local_start_time(self):
        return localtime(self.date_joined)
    
class UserAccount(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=CASCADE,)
    contact_no=models.CharField(max_length=11,null=True, default='00000000000')
    referral_code=models.CharField(max_length=200,null=True, blank=True)
    usertype=models.CharField(max_length=50,default='BUYER', choices=[('BUYER','BUYER'),('SELLER','SELLER'),('ADMIN','ADMIN')]) 
    status=models.CharField(max_length=50,default='ACTIVE',choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE'),('BANNED','BANNED')])
    def __str__(self):
        return str(self.user.username+' - '+self.usertype)
        
    def __str__(self):
        return str(self.user.username)
    

class UserWallet(models.Model):
    user=models.OneToOneField(UserProfile, on_delete=CASCADE)
    w_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    w_balance=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    w_points=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    w_commission=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    w_status=models.CharField(max_length=50,default='ACTIVE',choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE'),('BANNED','BANNED')])

    def __str__(self):
        return str(self.user.username +' - '+str(self.w_id))
    