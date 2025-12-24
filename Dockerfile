# 1. Start with a lightweight Python base image
FROM python:3.13-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# 4. Install dependencies
# We use --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code
COPY . .

# 6. Expose the port Streamlit runs on
EXPOSE 8501

# 7. Define the command to run your app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]