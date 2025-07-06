FROM php:8.1-apache

# Install mysqli extension
RUN docker-php-ext-install mysqli

# Enable Apache modules
RUN a2enmod rewrite

# Remove default Apache index file
RUN rm -f /var/www/html/index.html

# Copy challenge files
COPY vulnerable_login.php /var/www/html/index.php

# Set proper permissions
RUN chown -R www-data:www-data /var/www/html/
RUN chmod -R 644 /var/www/html/*.php

# Expose port 80
EXPOSE 80

# Start Apache in foreground
CMD ["apache2-foreground"]