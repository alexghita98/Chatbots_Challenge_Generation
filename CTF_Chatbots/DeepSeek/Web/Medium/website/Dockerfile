FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install --production --no-cache --progress=false
COPY server.js .
EXPOSE 3000
CMD ["node", "server.js"]