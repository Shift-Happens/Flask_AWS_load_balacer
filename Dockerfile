FROM python:3.12.7-slim

# Ustawienie zmiennych środowiskowych
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików requirements
COPY requirements.txt .

# Instalacja zależności Pythona
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie kodu aplikacji
COPY . .

# Ekspozycja portu
EXPOSE 5000

# Uruchomienie aplikacji
CMD ["python", "app.py"]