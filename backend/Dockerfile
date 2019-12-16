FROM python

WORKDIR /app

COPY . /app 

RUN pip install -r requirements.txt
RUN flask db init && flask db migrate && flask db upgrade
ENV FLASK_ENV development
ENV FLASK_APP main.py
EXPOSE 80
CMD ["flask","run","-h","0.0.0.0","-p","80"]
