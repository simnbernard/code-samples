FROM node:alpine as install
WORKDIR /app-build
COPY package.json ./package.json
COPY package-lock.json ./package-lock.json
RUN npm ci --no-optional && npm cache clean --force

FROM install as build
COPY . ./
RUN npm run build

FROM nginx:alpine
COPY --from=install /app-build/build /usr/share/nginx/html
COPY --from=install /app-build/nginx.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /app-build

EXPOSE 8080