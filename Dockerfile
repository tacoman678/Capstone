# Base Image
FROM python:3.10.10

# Set working directory
WORKDIR /app

# Install Chrome
RUN apt-get update && apt-get install -y wget gnupg2 unzip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Install chromedriver
RUN wget https://chromedriver.storage.googleapis.com/95.0.4638.17/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    chmod +x chromedriver && \
    mv chromedriver /usr/local/bin

# # Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# # Copy application files
COPY main.py .
COPY ScrapeAmazon.py .
COPY ScrapeEbay.py .
COPY static/  .
COPY templates/  .
COPY app.yaml  .

# # Start Flask server
# #CMD [ "python", "main.py" ]
