#!/bin/bash

old_password=$(cat /credentials/password.txt | awk 'NR==2' |awk -F ":" '{print $2}' )
new_password=$(</dev/urandom tr -dc '12345!#$%^&*()qwertQWERTasdfgASDFGzxcvbZXCVB' | head -c10)

systemctl restart mysqld
mysqladmin -uroot -p${old_password} -h localhost password $new_password

echo -e 'MySQL username:root\nMySQL Password:'$new_password  > /credentials/password.txt

                                                                                         
sed -i "s/\/root\/init.sh//" /etc/rc.local                                                      
rm -rf /root/init.sh

