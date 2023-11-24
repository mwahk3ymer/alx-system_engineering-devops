# This Puppet manifest installs Flask version 2.1.0 using pip3.

exec { 'flask':
  command  => '/usr/bin/apt-get -y install puppet-lint -v 2.1.0',
  provider => 'pip3',
}
