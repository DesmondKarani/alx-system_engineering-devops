# Puppet manifest to fix a 500 Internal Server Error for a Wordpress site
# This script assumes incorrect permissions and a misconfigured .htaccess file
# as potential causes for the error.

# Ensure correct permissions for the Wordpress directory
file { '/var/www/html/wordpress':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Replace the .htaccess file with a known good configuration
file { '/var/www/html/wordpress/.htaccess':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => "\
<IfModule mod_rewrite.c>\n\
RewriteEngine On\n\
RewriteBase /\n\
RewriteRule ^index\.php$ - [L]\n\
RewriteCond %{REQUEST_FILENAME} !-f\n\
RewriteCond %{REQUEST_FILENAME} !-d\n\
RewriteRule . /index.php [L]\n\
</IfModule>\n",
  require => File['/var/www/html/wordpress'],
}

# Ensure Apache service is running and will restart if any changes are made
service { 'apache2':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/var/www/html/wordpress/.htaccess'],
}
