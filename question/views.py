from django.shortcuts import render
from question.models import Question, Answer
from django.http import HttpResponseRedirect


# Create your views here.
def q_and_a(request):
    state = None
    questions = Question.objects.order_by('-time')
    answers = Answer.objects.order_by('time')
    print(answers[0].questions_id)
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'question': questions,
            'answer': answers,
        }
    else:
        content = {
            'state': state,
            'question': questions,
            'answer': answers,
        }
    return render(request, 'q&a.html', content)


def add_question(request):
    new_questioner = request.user.first_name
    new_content = str(request.POST['question_content'])
    if new_content == '':
        return q_and_a(request)
    new_question = Question.objects.create(questioner=new_questioner, content=new_content)
    new_question.save()
    return HttpResponseRedirect('q&a.html')


def add_answer(request):
    new_answerer = request.user.first_name
    new_content = str(request.POST['answer_content'])
    if new_content == '':
        return q_and_a(request)
    new_question_id = int(request.POST['question_id'])
    new_answer = Answer.objects.create(answerer=new_answerer, content=new_content, questions_id=new_question_id)
    new_answer.save()
    return HttpResponseRedirect('q&a.html')
