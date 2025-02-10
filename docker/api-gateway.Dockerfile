FROM python:3.12-alpine

WORKDIR /app

RUN pip install uv

RUN apk add --no-cache gcc musl-dev python3-dev zlib-dev

COPY backend/api_gateway/ .

COPY .env .

RUN uv sync

EXPOSE 15015

CMD ["uv", "run", "api-gateway"]
