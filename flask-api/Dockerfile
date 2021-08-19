FROM python:3.7

# run operations inside the container
RUN mkdir /usr/src/app/

# copy the app to the container
COPY . /usr/src/app/

# set path where CMD and RUN commands are scoped
WORKDIR /usr/src/app/

# expose port 5000 for external access
EXPOSE 5000

# install the dependencies
RUN pip install -r requirements.txt

# spin up the server
CMD [ "python", "app.py" ]