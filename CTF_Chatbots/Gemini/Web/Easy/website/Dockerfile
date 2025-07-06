# Use a lightweight Nginx base image
FROM nginx:alpine

# Copy the custom index.html file into the Nginx web root
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Command to run Nginx (default for nginx:alpine)
CMD ["nginx", "-g", "daemon off;"]