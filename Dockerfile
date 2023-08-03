# Start with a base image containing Python runtime
FROM python:latest

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY entrypoint.sh /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# we need wget to set up the Geckodriver

RUN apt-get update && apt-get install -y wget git rsync curl

# Install GeckoDriver


# Make port 8080 available to the world outside this container
EXPOSE 8080


#CMD python starter.py && python xxx.py
ENTRYPOINT ["bash", "entrypoint.sh"]
