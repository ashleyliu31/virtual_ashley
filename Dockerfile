FROM python:3.10.13-bookworm
RUN apt-get update && \
    apt-get install -y --no-install-recommends sqlite3 && \
    sqlite3 --version && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN sqlite3 --version
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app