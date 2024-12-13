FROM PYTHON

ADD bot.py .
ADD bot_announcements.py .
ADD commands.py .
ADD config.json .
ADD exceptions.py .
ADD requirements.txt .
ADD tvdb.py .
ADD xmltvparse.py .

ARG DISCORDKEY
ARG TVDBKEY
ARG XMLTVURL
ARG MAINCHANNEL
ARG ANNOUNCEMENTS_ENABLED
ARG ANNOUNCEMENTS_CHANNEL_ID
ARG CHANNEL_NAME
ARG ADMIN_ROLE_NAME

ENV DISCORDKEY = $DISCORDKEY
ENV TVDBKEY = $TVDBKEY

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]