from django.db import models

# Create your models here.

class UserInterest(models.Model):
    user_name = models.CharField(max_length = 100)
    user_interest = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.user_name + ' - ' + self.user_interest

class NewsFeed(models.Model):
    user_name = models.CharField(max_length = 100)
    content = models.TextField(max_length = 999)
    
    def __str__(self):
        return self.user_name + ' -> ' + self.content

class score(models.Model):
    newsfeed = models.ForeignKey(NewsFeed,on_delete = models.CASCADE)
    category = models.CharField(max_length = 100)
    score = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.category + ' ' + self.score + ' ' + str(self.newsfeed.content)