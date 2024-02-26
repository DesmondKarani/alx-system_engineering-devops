# This Puppet manifest uses the exec resource to kill a process named 'killmenow'

exec { 'kill_killmenow_process':
  command   => '/usr/bin/pkill -f killmenow',
  onlyif    => '/usr/bin/pgrep -f killmenow',
  path      => ['/bin', '/usr/bin'],
}
