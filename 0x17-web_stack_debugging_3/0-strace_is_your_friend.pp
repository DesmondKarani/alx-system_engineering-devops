# Puppet manifest to fix a 500 Internal Server Error for a Wordpress site

exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin',
}

