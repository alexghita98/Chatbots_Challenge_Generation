FROM php:8.1-apache

# Enable mod_rewrite for cleaner URLs if needed
RUN a2enmod rewrite

# Copy PHP application files to the Apache web root
COPY . /var/www/html/

# Set appropriate permissions
RUN chown -R www-data:www-data /var/www/html/
RUN chmod -R 755 /var/www/html/

# Expose port 80
EXPOSE 80

# Apache will be run by default
CMD ["apache2-foreground"]