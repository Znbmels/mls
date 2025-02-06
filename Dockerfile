# Используем официальный Python-образ
FROM python:3.12

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для Django
EXPOSE 8000

# Запуск сервера Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "quranlearning.wsgi:application"]
