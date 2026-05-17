# 1. Python ka environment use karein
FROM python:3.9-slim

# 2. Container ke andar /app folder banayein
WORKDIR /app

# 3. Sirf requirements file pehle copy karein
COPY requirements.txt .

# 4. Libraries install karein
RUN pip install --no-cache-dir -r requirements.txt

# 5. Apna baqi sara code (app.py) copy karein
COPY . .

# 6. Port 8000 open karein
EXPOSE 8000

# 7. App start karne ki command
CMD ["python", "app.py"]