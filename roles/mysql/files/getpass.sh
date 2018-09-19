#!/bin/bash

pass=$(grep "A temporary password is generated for root@localhost:" /var/log/messages |awk '{print $16}')

cat > /root/.my.cnf <<EOF
[client]
user=root
password=$pass
EOF