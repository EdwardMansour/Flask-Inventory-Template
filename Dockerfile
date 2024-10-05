FROM python:3.11.10-bullseye

WORKDIR /src

COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
