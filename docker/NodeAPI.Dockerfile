FROM node:alpine as install
WORKDIR /app-build
COPY package*.json ./
RUN npm ci && npm cache clean --force
COPY . .

FROM install as build
RUN npm run build && npm prune --production

FROM node:alpine
WORKDIR /app
COPY --from=build /app-build ./
RUN rm -rf ./src ./.eslintrc ./tsconfig.json ./nodemon.json

EXPOSE 8081
CMD ["node", "build/index.js"]
