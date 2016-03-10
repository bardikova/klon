# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, redirect
from questions.models import Questions
from django.http import Http404
from django import forms


def hello_world(request):
    return HttpResponse(u'Привет')

def question_list(request):
    question = Questions.objects.all() #question = Questions.object.all().order_by('-created_at') сортировка по времени создания
    return render(request, 'main/question_list.html', {
        'questions': question
        })

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('title', 'text', 'user_email', 'phone_number', 'request_number', 'status', )

def question_create(request):
    form = QuestionForm(request.GET or None)
    if form.is_valid():
        form.save()
    
    # if 'request_number' not in request.GET:
    #     return render(request, 'main/question_create.html')
    # request_number = request.GET['request_number']
    # title = request.GET['title']
    # text = request.GET['text']
    # phone_number = request.GET['phone_number']
    # user_email = request.GET['user_email']
    # status = request.GET['status']

    # Questions.objects.create(
    #     request_number=request_number, title=title, text=text,
    #     phone_number=phone_number, user_email=user_email, status=status
    # )
    return render(request, 'main/question_create.html', {'form': form})


def delete_question(request, question_id):
    if not request.user.is_superuser:
        raise Http404
    question = Questions.objects.get(id=question_id)
    question.delete()
    return redirect('/')

# def question_status_published(request, question_id):
#     question_status = Questions.objects.get(id=question_id)
#     question_status.status = 'published'
#     question.save()
#     return HttpResponse("тест")

# def question_status_new(request, question_id):
#     question = Questions.objects.get(id=question_id)
#     question.status = 'new'
#     question.save()
#     return redirect('/')

def change_status(request, question_id, status_name):
    q = Questions.objects.get(id=question_id)
    q.status = status_name
    q.save()
    return redirect('/')

def question_detail(request, question_id):
    question = Questions.objects.get(id=question_id)
    return render(request, 'main/one_question.html', {
        'question': question
        })

    # {% url 'change_status' question_id 'published %}
    # {% url 'change_status' question_id 'decline %}
    # {% url 'change_status' question_id 'canceled%}

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Questions
#         exclude = ()


