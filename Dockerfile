FROM python:3.12

COPY app.py app.py

# -u prevents python buffering the logs
ENTRYPOINT ["python", "-u", "app.py"]
