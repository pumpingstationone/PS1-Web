FROM python:3
LABEL authors="cjoshmartin"
ENV PYTHONUNBUFFERED=1
ENV PORT=80
WORKDIR /code
COPY . /code/

RUN  ln -s /usr/local/bin/pip /usr/bin/pip && pip install --upgrade pip
RUN pip install --root-user-action=ignore -r requirements.txt

#EXPOSE 80
#CMD exec gunicorn -b :80 -w 2 ps1backend.wsgi

