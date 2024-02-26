# Install pip3 package provider
package { 'python3-pip':
  ensure => installed,
}

# Install flask from pip3 with version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
