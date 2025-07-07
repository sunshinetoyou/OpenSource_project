# Python 공식 이미지 사용
FROM python:3.12

# 작업 디렉토리 생성
WORKDIR /app

# Django만 직접 설치
RUN pip install --upgrade pip && pip install django

# 소스 코드 복사
COPY . .

# 포트 오픈
EXPOSE 8000

# 마이그레이션 및 서버 실행
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]