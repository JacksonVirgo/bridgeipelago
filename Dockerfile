FROM python:3.12

WORKDIR /bridgeipelago

RUN git clone https://github.com/Quasky/bridgeipelago.git .

COPY ./run.sh ./run.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "bridgeipelago.py"]

