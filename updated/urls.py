from django.urls import path
from . import views

app_name = 'updated'

urlpatterns = [
    path('addUserInterest/',views.addUserInterest,name='addUserInterest'),
    path('addNewsFeed/',views.addNewsFeed,name='addNewsFeed'),
    path('loadNewsFeed/',views.loadNewsFeed,name='loadNewsFeed'),
    path('viewNewsFeed/',views.viewNewsFeed,name='viewNewsFeed'),
]
