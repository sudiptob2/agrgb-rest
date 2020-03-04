FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install tensorflow_cpu-2.1.0-cp37-cp37m-manylinux2010_x86_64.whl
EXPOSE 5000
WORKDIR /app/app
ENV FLASK_APP=run.py
CMD ["flask", "run", "--host", "0.0.0.0"]
