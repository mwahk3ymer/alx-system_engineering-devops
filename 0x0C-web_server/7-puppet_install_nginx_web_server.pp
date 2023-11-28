# File: nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Start and enable Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define default Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80;
    server_name localhost;

    location / {
        echo 'Hello World!';
        root /var/www/html;
        index index.html;
    }

    location /redirect_me {
        return 301 http://www.example.com/redirected_page;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Reload Nginx to apply the new configuration
exec { 'nginx_reload':
  command     => 'service nginx reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
