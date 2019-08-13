# Add config to simplify connecting to Holberton server
file_line { 'disable SSH password':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  match   => '^#?\s*PasswordAuthentication\s+\S+$'
}

file_line { 'use Holberton ssh key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton',
  match   => '^(    |\t)IdentityFile ~/\.ssh/holberton$'
}
