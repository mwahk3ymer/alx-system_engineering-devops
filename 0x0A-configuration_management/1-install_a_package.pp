#this Puppet manifest installs puppet-lint version 2.5.0

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  require  => Exec['update_gems'],
}

exec { 'update_gems':
  command => 'gem update --system',
  path    => '/usr/bin',
}
