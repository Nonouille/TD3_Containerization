FROM python:3.8
RUN useradd -ms /bin/bash user1
USER user1
WORKDIR /app
COPY . /app
RUN pip install fuzzywuzzy
RUN pip install python-Levenshtein
CMD ["python","app.py"]

