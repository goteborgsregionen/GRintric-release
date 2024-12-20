# Stage 1: Build the frontend application
FROM node:22-alpine AS builder

WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm@8.9.0

# Copy package files
COPY package*.json pnpm-lock.yaml ./

# Install dependencies with caching
RUN --mount=type=cache,id=pnpm,target=/root/.local/share/pnpm/store pnpm install --frozen-lockfile

# Copy source code
COPY . .

# Build the application (if needed for production)
RUN pnpm run build

# Development stage
FROM node:22-alpine AS develop

WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm@8.9.0

# Copy package files
COPY package*.json pnpm-lock.yaml ./

# Install dependencies with caching
RUN --mount=type=cache,id=pnpm,target=/root/.local/share/pnpm/store pnpm install

# Copy source code
COPY . .

EXPOSE 3000

CMD pnpm -w run dev