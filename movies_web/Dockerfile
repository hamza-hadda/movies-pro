# syntax=docker/dockerfile:1.4
FROM node:14.4.0-alpine

RUN mkdir /project
WORKDIR /project

COPY . .

RUN npm install -g @vue/cli
RUN npm install