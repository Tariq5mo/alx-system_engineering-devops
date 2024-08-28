# Install a package by puppet

package { 'Install flask with specific version':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}
