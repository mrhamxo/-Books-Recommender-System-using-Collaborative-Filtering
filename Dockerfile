# use python 3.11 base image
FROM python:3.11-slim

# set the working directory
WORKDIR /app    

# copy the requirements file and install dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code
COPY . /app

# expose the application port
EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

