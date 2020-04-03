
FROM python:3

ADD * /

RUN pip install python-telegram-bot
RUN pip install python-binance
RUN pip install schedule

CMD [ "python", "./calls.py" ]