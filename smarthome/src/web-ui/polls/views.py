from django.http import HttpResponse
from .models import Question
from django.template import loader
import json

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def get_data(request):
    res = {"categories": ["周一","周二","周三","周四","周五","周六","周日"],"data1":[500,280,386,190,107,207,452],"data2":[12,223,345,66,89,453,996]}
    return HttpResponse(json.dumps(res), content_type="application/json")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)