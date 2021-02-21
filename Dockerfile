FROM python:3.9


RUN pip install swagger-spec-validator==2.7.3
COPY validate.py .

ENTRYPOINT ["python", "validate.py"]
