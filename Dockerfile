FROM python:3.8.7-alpine3.13
RUN pip3 install  bottle GitPython \
    && apk add git
COPY server-note.py .
ENTRYPOINT ["python","server-note.py"] 
