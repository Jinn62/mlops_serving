FROM python:3.13-slim

WORKDIR /root/mlops_serving

RUN pip install --no-cache-dir fastapi uvicorn scikit-learn joblib python-multipart

COPY main.py .
COPY model.joblib .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]