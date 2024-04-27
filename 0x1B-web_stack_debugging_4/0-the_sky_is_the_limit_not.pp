# This configuration adjusts the hard and soft file limits for the 'holberton' user,
# enabling better handling of concurrent connections and file operations under load.

exec { 'increase-hard-file-limit-for-holberton-user':
  command => "/usr/bin/sed -i '/^holberton hard nofile/ s/[0-9]*/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin:/usr/bin',
  unless  => "/bin/grep -q '^holberton hard nofile 50000' /etc/security/limits.conf",
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => "/usr/bin/sed -i '/^holberton soft nofile/ s/[0-9]*/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin:/usr/bin',
  unless  => "/bin/grep -q '^holberton soft nofile 50000' /etc/security/limits.conf",
}
