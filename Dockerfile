FROM node:alpine


WORKDIR /usr/src/hackerrank-testcase-generator

COPY ./ ./

RUN npm install


CMD ["sh"]