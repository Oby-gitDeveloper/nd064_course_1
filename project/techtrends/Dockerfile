FROM python:3.9
COPY . /app
RUN make /app
EXPOSE 3111

# command to run on container start
CMD [ "python", "init_db.py" ]
