FROM python:3.9-buster
LABEL Ivan Grujicic <gruja90@gmail.com>


# Check our python environment
RUN python --version
RUN pip --version

# Set the working directory for containers
RUN mkdir /opt/src
WORKDIR  /opt/src/

# Installing python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files from the project’s root to the working directory
COPY app/ /opt/src/app
COPY logging.conf /opt/src/logging.conf
COPY Makefile /opt/src/Makefile

# Expose ports for flask, redis and postgresqls
EXPOSE 5000

# Running Python Application
RUN cd /opt/src
CMD ["make", "run"]