from django.db import models

class Question(models.Model): # 모델 클래스 상속받음
    # ORM: 데이터베이스 테이블과 매핑됨 (id 속성 자동 생성)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # '설명'

    # 객체 출력 시 텍스트 내용이 출력 (메모리 주소 출력 방지)
    def __str__(self):
        return self.question_text

class Choice(models.Model):

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 종속개념


    def __str__(self):
        return self.choice_text

