FROM python:3.12

WORKDIR /bridgeipelago

RUN git clone https://github.com/JacksonVirgo/bridgeipelago.git .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY config.json.template ./config.json
CMD /bin/sh -c "envsubst < config.json > config.json && python bridgeipelago.py"

CMD ["sh", "-c", "python config.py && python bridgeipelago.py"]

