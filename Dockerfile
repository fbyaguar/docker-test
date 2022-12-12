# Pull base image
FROM python:3.8

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /test-drf

# Install postgres dependencies
RUN apt-get update \
    && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y

# Copy project
COPY . /test-drf
# RUN sed -i 's/\r$//g' entrypoint.sh
# RUN chmod +x entrypoint.sh

# Install dependencies
RUN pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT [ "sh", "entrypoint.sh" ]