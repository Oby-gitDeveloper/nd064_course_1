FROM python:3.9
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 3111

# command to run on container start
CMD [ "python", "init_db.py" ]
