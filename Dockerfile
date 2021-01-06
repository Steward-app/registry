FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt

CMD ["python", "-m", "registry.monolithic_server", "--flagfile=prod.flags"]
