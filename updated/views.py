from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse
from updated.models import *
# from newsfeed.form import addCategoryFor
from django.shortcuts import render
import json
import paralleldots
# Create your views here.

paralleldots.set_api_key( "nUV2Ym1gQr8REXKIZQzgKQkDBUkBaUSK6Qukfcx4LwE" )

# Function to let user add his own interest
@csrf_exempt
def addUserInterest(request):
    template = loader.get_template('addUserInterest.html')
    if request.method == 'GET':
        return HttpResponse(template.render())
    else:
        input_user_name = request.POST.get('user_name')
        input_interest =request.POST.get('user_interest')
        user_interest = UserInterest()
        user_interest.user_name = input_user_name
        user_interest.user_interest = input_interest
        user_interest.save()
        return HttpResponse("Interest added")

@csrf_exempt
def addNewsFeed(request):
    template = loader.get_template('addNewsFeed.html')
    if request.method == 'GET':
        return HttpResponse(template.render())
    else:
        input_user_name = request.POST.get('user_name')
        input_content =request.POST.get('user_content')
        user_interest = NewsFeed()
        user_interest.user_name = input_user_name
        user_interest.content = input_content
        user_interest.save()
        print(user_interest.pk)
        # To update score
        # Manually adding categories
        category = {
            'language':["c++","java","c","c#"],
            'sports':["cricket","football"],
            'gaming':["pubg","coc"],
            'NIT':["NIT Jalandhar","NIT Trichy"]
        }
        api_scores = paralleldots.custom_classifier( input_content, category )
        # api_scores = json.loads(api_scores)
        print(api_scores)
        print(api_scores['taxonomy'])
        for api_score in api_scores['taxonomy']:
            tag = api_score['tag']
            score_ = api_score['confidence_score']
            score_table = score()
            score_table.newsfeed = user_interest
            score_table.category = tag
            score_table.score = score_
            score_table.save()
        
        return HttpResponse("Interest added")

@csrf_exempt
def viewNewsFeed(request):
    template = loader.get_template('loadNewsFeed.html')
    if request.method == 'GET':
        return HttpResponse(template.render())
        
@csrf_exempt
def loadNewsFeed(request):
    newsfeeds = NewsFeed.objects.all()
    res = {}
    i = 0
    for newsfeed in newsfeeds:
        score_ = score.objects.filter(newsfeed = newsfeed)
        a = {}
        tag = []
        a['user_name'] = newsfeed.user_name
        a['content'] = newsfeed.content
        a['score'] = {}
        for score__ in score_:
            a['score'][score__.category] = float(score__.score)
            tag.append(score__.category)
        a['tags'] = tag
        res[str(i)] = a
        i=i+1
    res['length'] = i
    print(res)
    return JsonResponse(res)