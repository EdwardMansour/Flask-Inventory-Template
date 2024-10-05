FROM python:3.11.10-bullseye

WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

CMD ["/bin/bash", "entrypoint.sh"]