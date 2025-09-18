FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --root-user-action=ignore
COPY main.py .
EXPOSE 10001
CMD ["/bin/sh", "-c", "exec gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT --workers 4 --timeout 120"]
