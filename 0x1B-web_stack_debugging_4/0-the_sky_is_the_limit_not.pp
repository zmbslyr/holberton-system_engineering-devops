#Fixes low file limit in nginx server
file { 'replace last line':
  ensure   => present,
  path     => '/etc/default/nginx',
  content  => 'ULIMIT="-n 4096"',
}

service { 'Nginx':
  ensure      => running,
  hasrestart  => true,
  subscribe   => File['/etc/default/nginx']
}
