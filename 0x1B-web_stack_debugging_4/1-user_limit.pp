# Remove small open file limit for user
file { 'remove user limit':
  ensure  => file,
  path    => '/etc/security/limits.conf',
  content => '\n'
}
