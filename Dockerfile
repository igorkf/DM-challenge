FROM python:3.9.4-alpine

RUN pip install fastapi uvicorn python-multipart

EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]