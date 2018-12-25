from django.db import models

# Create your models here.


class userTable(models.Model):
    CHOICE = (
        ('normal','Normal'),
        ('institute_admin','Institute Admin'),
        ('super_admin','Super Admin'),
    )
    user_name = models.CharField(max_length = 100)
    user_type = models.CharField(max_length = 20, choices = CHOICE,default = 'normal')
    first_name = models.CharField(max_length = 100, default='')
    last_name = models.CharField(max_length = 100, default='')
    organization = models.CharField(max_length = 100, default='')
    profile_pic = models.FileField(upload_to='profilePics/',default='profilePics/default.png')
    def __str__(self):
        return str(self.pk) + ' | ' + self.user_name + ' | ' + self.user_type
    
class userLoginTable(models.Model):
    ACCOUNT_STATUS = (
        ('active','ACTIVE'),
        ('blocked','BLOCKED'),
    )
    user_name = models.ForeignKey('userTable',on_delete = models.CASCADE)
    password = models.CharField(max_length = 20)
    user_status = models.CharField(max_length = 20,choices = ACCOUNT_STATUS)
    
    def __str__(self):
        return str(self.user_name) + ' | ' + self.password + ' | ' + self.user_status