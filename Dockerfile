# 1. Use Python base image
FROM python:3.9-slim

# 2. Create /app folder inside the container
WORKDIR /app

# 3. Copy only requirements file first
COPY requirements.txt .

# 4. Install libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the code (app.py)
COPY . .

# 6. Open port 8000
EXPOSE 8000

# 7. Command to start the app
CMD ["python", "app.py"]