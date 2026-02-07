FROM python:3.12

WORKDIR /bridgeipelago

RUN git clone https://github.com/Quasky/bridgeipelago.git .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY config.json.template ./config.json
CMD /bin/sh -c "envsubst < config.json > config.json && python bridgeipelago.py"

CMD ["python", "bridgeipelago.py"]

