# === STAGE 1: Build Vue app ===
FROM node:20-alpine AS build-stage

WORKDIR /app
COPY . .

RUN npm i -g pnpm && pnpm install && pnpm run build

# === STAGE 2: FastAPI backend with built frontend ===
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

# Copia backend y archivo de cookies base64
COPY main.py requirements.txt /app/

COPY --from=build-stage /app/dist ./dist

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]