FROM python:3.8
WORKDIR /project
COPY . /project/
COPY requirements.txt .
RUN ["python", "-m", "pip", "install", "-U", "pip"]
RUN ["pip", "install", "-r", "requirements.rtf"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]