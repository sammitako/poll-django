from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'q_list': question_list}  # 모델 데이터
    return render(request, 'polls/templates/polls/index.html', context)

def detail(request, question_id):
    # question_id(설문 pk) 숫자가 들어옴
    question = get_object_or_404(Question, pk=question_id) # Question의 pk = id 컬럼
    context = {'selected_question': question}
    return render(request, 'polls/detail.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['my_choice'])
    except(KeyError, Choice.DoesNotExist):
        # PK가 없어서 오류가 발생할 경우
        return render(request, 'polls/detail.html', {'selected_question': question,
                                                     'error_message': 'Nothing was chosen'}) # {context}
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id, ))) # 인자가 1개인 튜플 형태
        # context = {'selected_question': question}
        # return render(request, 'polls/detail.html', context) # HttpResponse 객체가 리턴됨 (클라이언트가 이 결과 HTML를 브라우징함)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question
    })
