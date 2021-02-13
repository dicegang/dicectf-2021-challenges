FROM node:15-buster-slim

WORKDIR /app

COPY package.json /app/

RUN yarn

COPY . .

ENV NODE_ENV production
ENV FLAG c0uldn7_f1nd_4_b4ckr0nym_f0r_1de

EXPOSE 3000

CMD ["node", "/app/index.js"]
