FROM python:3.10-slim
ENV TOLEN='6848157270:AAGZcvamwh0neIvcN5Cb4KbaayRNiCmD6VQ'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]