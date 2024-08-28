# Execute a command

exec { 'kill process':
  command => '/usr/bin/pkill -f killmenow',
  cwd     => '/',
}
