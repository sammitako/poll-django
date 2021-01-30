from django.urls import path
from . import views

# 고정 url: http://localhost:8000/polls/
app_name = 'polls' # namespace
urlpatterns = [
    path('', views.index, name='index'), # polls:index

    # polls/숫자/
    # 변하는 값 명시 <숫자:데이터>
    path('<int:question_id>/', views.detail, name='detail'), # detail: 해당 설문에 대한 항목 리스트
    path('<int:question_id>/vote/', views.vote, name='vote'), # polls:vote

    # http://localhost:8000/polls/1/results/
    path('<int:question_id>/results/', views.results, name='results') # polls:results

]
