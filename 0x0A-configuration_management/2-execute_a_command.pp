# This Puppet manifest uses the exec resource to kill a process named 'killmenow'

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
