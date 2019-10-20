from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
from django.shortcuts import render, get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'poll/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.object.get(pk=question_id)
    # except:
    #     raise Http404("Question does not exist.")
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You are looking at question %s"
    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse("You are looking at question %s"%question_id)
