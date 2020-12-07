#xd 

file { '/tmp/holberton':
  ensure  => file,
  path    => '/tmp/holbertonschool',
  mode    => '0744'
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
