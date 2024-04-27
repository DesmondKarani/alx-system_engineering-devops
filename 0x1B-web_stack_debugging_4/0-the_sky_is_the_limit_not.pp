# This block allows the user "holberton" to access and modify a greater number of files simultaneously.
# It increases the maximum number of files the user "holberton" can have open at one time.

exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/ s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin',
}

# This block enhances system flexibility for the "holberton" user by increasing the soft file limit.
# It raises the initial file descriptor limit for the "holberton" user.

exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '/^holberton soft/ s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin',
}
