FROM python:3.8-slim
WORKDIR /app
COPY assignment.py /app
RUN pip install flask
CMD ["python", "assignment.py"]
