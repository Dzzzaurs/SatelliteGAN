# Base image
FROM node:14-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci --only=production

# Copy the project files to the working directory
COPY . .

# Build the React app
RUN npm run build

# Expose the application port
EXPOSE 3000

# Run the application
CMD ["npm", "start"]