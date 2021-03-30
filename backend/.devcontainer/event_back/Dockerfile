FROM python:3.9-slim
WORKDIR /usr/event_back

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8
COPY requirements.txt .
# requirements.txtにリストされたパッケージをインストールする
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
# stdout/stderrバッファを無効にする
ENV PYTHONUNBUFFERED 1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","8084"]

EXPOSE 8084