# My Site
# Version: 1.0
FROM python:3.7
# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

# Project Files and Settings
ARG PROJECT=ParcYourShop
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
ADD . $PROJECT_DIR
RUN pip install -r requirements.txt
# Server
EXPOSE 8000
STOPSIGNAL SIGINT
RUN python manage.py makemigrations
RUN python manage.py migrate
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]