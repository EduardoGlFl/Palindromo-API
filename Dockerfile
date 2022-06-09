FROM alpine:3.10

RUN apk add --no-cache python3-dev\
    && pip3 install --upgrade pip

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY app.py .

CMD ["gunicorn", "-b", "0.0.0.0:7000" ,"app:app"]