from django.db import models

class Project(models.Model):
    subject = models.CharField(max_length=200)  # 제목에 200자 제한
    detail = models.TextField()
    avg_score = models.FloatField(null=True, blank=True)  # 평균 점수 필드 추가

class Vote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # FK 설정
    score = models.IntegerField(choices=[(i, i) for i in range(1,6)])   # 1~5 사이의 정수값만 입력 받음
