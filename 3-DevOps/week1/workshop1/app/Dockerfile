FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
# RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /usr/src/app
# USER appuser
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "nc_tutorials.wsgi"]
