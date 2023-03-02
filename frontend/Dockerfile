# FROM node:18.13
FROM node:16.19


WORKDIR /app/frontend

RUN apt-get update && apt-get install git

COPY package*.json .

RUN npm install && npm cache clean --force

# RUN mkdir node_modules/.vite && chmod -R 777 node_modules/.vite

COPY . .

ENV HOST 0.0.0.0 
EXPOSE 3000

