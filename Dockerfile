FROM anasty17/mltb:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN playwright install chromium
RUN apt-get update && apt-get upgrade -y
RUN apt -qq update --fix-missing && \
    apt -qq install -y mediainfo wget
RUN wget https://drive.nanthakps.workers.dev/2:/config-files/accounts.zip \
    https://drive.nanthakps.workers.dev/2:/config-files/token.pickle
    
COPY . .

CMD ["bash", "start.sh"]
