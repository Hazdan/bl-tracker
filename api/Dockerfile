FROM ubuntu:20.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/server.py"]