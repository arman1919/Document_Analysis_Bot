FROM python:3.10

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD ["python", "/app/bot_doc_analiz_TG.py"]
