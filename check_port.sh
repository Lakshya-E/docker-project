if ( nc -zv localhost 80 2>&1 >/dev/null ); then
    echo 'Online'
else
    echo 'Offline'
fi
