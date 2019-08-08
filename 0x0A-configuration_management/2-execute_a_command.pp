# Execute a command
exec { 'kill me script':
	command	=> '/usr/bin/pkill --exact killmenow'
}
