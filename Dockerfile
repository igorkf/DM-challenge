FROM python:3.9.4-alpine

RUN pip install pip --upgrade
RUN pip install fastapi uvicorn PyJWT python-decouple pydantic[email]

EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]