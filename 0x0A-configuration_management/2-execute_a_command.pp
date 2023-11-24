# This Puppet manifest kills the process named "killmenow"

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
  subscribe   => File['/path/to/your/killmenow_script'],
}

file { '/path/to/your/killmenow_script':
  ensure  => present,
  mode    => '0755',
  content => "#!/bin/bash\nwhile [[ true ]]; do sleep 2; done\n",
}
