# Puppet script for task 0

exec { 'update':
  command => '/usr/bin/pat-get update',
}

package { 'nginx':
  ensure  => Installed,
  require => Exec['update'],
}

file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases/':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'fake html page',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

exec { 'sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}':
  target => 'hbnb_static',
  path   => '/etc/nginx/sites-enabled/default',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
}

exec { 'nginx restart':
  path => '/etc/init.d/',
}