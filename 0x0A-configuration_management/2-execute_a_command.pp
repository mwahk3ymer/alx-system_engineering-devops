# This Puppet manifest kills the process named "killmenow"

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
  subscribe   => File['/path/to/your/killmenow_script'],
}
