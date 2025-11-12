FROM python:3.12-slim

# Evitar que Python guarde pyc y buffer stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

# CMD ["gunicorn", "--bind", "0.0.0.0:5050", "app:app"]
# CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5050", "app:app"]
CMD ["python", "app.py"]