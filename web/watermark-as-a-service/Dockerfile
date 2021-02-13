FROM node:15.8.0-buster-slim

RUN apt-get update \
    && apt-get install -y wget gnupg ca-certificates \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package.json yarn.lock /app/
RUN yarn --prod --frozen-lockfile

COPY . ./

ENV FLAG dice{the_cloud_is_just_someone_elses_computer}

USER node

CMD ["node", "app"]
