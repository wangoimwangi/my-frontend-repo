# Use the official Node.js image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install the app dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the app for production
RUN npm run build

# Install serve to serve the built app
RUN npm install -g serve

# Expose the port on which the app runs
EXPOSE 3000

# Command to run the application
CMD ["serve", "-s", "build"]
