#Deriving the latest base image
FROM python:latest


#Labels as key value pair"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY . .
# COPY test.py ./

# Now the structure looks like this '/usr/app/src/test.py'


EXPOSE 8080
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./server.py"]

