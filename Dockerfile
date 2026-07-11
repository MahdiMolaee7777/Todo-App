FROM python:3.11-slim

# تنظیم متغیرهای محیطی
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# تنظیم working directory
WORKDIR /app

# نصب dependencies سیستمی
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# کپی و نصب requirements
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# کپی کد پروژه
COPY . .

# ساخت دایرکتوری‌های static و media
RUN mkdir -p /app/staticfiles /app/media

# پورت
EXPOSE 8000

# دستور پیش‌فرض
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]