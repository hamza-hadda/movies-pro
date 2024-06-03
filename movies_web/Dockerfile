FROM node:20-alpine

RUN mkdir /project
WORKDIR /project

COPY . .

RUN npm install -g @vue/cli
RUN npm install

CMD ["npm", "run", "serve"]