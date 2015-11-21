from django.http import HttpResponse, Http404
from django.shortcuts import render
# from apps.quiz.models import Question, Choice
from models import Question, Choice

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    # context = {
    #     'questions': [
    #         {'id': 1, 'content': 'This is question 1'},
    #         {'id': 2, 'content': 'This is question 2'},
    #         {'id': 3, 'content': 'This is question 3'}
    #     ]
    # }
    return render(request, 'quiz/index.html', context)

def show(request, question_id):
    req_question = Question.objects.get(id=question_id)
    choices = Choice.objects.all().filter(question=req_question)
    context = {'question': req_question, 'choices': choices}
    # context = {
    #     'id': question_id,
    #     'question': 'Why is a boxing ring square?'
    # }
    return render(request, 'quiz/show.html', context)
    # return HttpResponse('You are looking for question %s' % question_id)
    # if int(question_id) == 1:
    #     return HttpResponse('<h1>Page found!!!</h1>')
    # else:
    #     return HttpResponseNotFound('<h1>Not found!!!</h1>')
