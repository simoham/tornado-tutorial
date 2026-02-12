FROM alpine:3.23.3

WORKDIR /app
RUN apk update && apk add python3 py3-pip py3-virtualenv

COPY . . 

RUN python -m venv /app
ENV PATH="/app/bin:$PATH"
RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "server.py"]
