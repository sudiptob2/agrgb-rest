FROM python:3.7
COPY app .
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "run.py" ] 