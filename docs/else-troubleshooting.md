# Troubleshooting

If you're having trouble with running LEMP, here is a quick guide to solve most common problems.

> Most faults about the Instance is closely related to the Instance provider, Cloud Platform. Provided you're sure the fault is caused by Cloud Platform, refer to [Cloud Platform Documentation](https://support.websoft9.com/docs/faq/tech-instance.html).

#### Redirects Error?

Check your *server{ }* segment in the [Nginx vhost configuration file](/stack-components.md#nginx), remove cycle redirects settings

#### Java application responds very slowly?

Java have a class named [SecureRandom](https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html), This class provides a cryptographically strong random number generator (RNG), it may cause JVM wait for more time but this class is not useful in Linux. Suggest you change the securerandom.source

#### Website pictures loading very slowly?

Please make sure that your bandwidth of Server is more than 5M

#### Database service could not be started?

Insufficient disk space, insufficient memory, and configuration file errors can make database service could not be started  

It is recommended to first check through the command.

```shell
# check the MySQL service
sudo systemctl restart mysql
sudo systemctl status mysql
sudo journalctl -u mysql

# view disk space
df -lh

# view memory rate
free -lh
```

#### The database log file is too large, resulting in insufficient disk space?

By default, mysql will automatically open the binlog. Binlog is mainly used to recover the database without backup. However, the binlog will take up a lot of space. If you don't clean it for a long time, the remaining disk space will be 0, which will affect the database or the server will not start.

If you have confidence in your own backup, you do not need the binlog function. Refer to the following steps to turn it off:

1. Edit [MySQL Configuration File] (/stack-components.md#mysql) and comment out the binlog log   
    ```
    #log-bin=mysql-bin
    ```
2. Restart mysql
    ```
    sudo systemctl restart mysql
    ```
#### phpMyAdmin page access blank?

Please try another browser, such as chrome or firefox. If the phpMyAdmin can be opened normally before, and now appears to be incomplete or blank, it is recommended to clean up the browser cache, cookies and other information

#### PhpMyAdmin Timeout Errors

If you try to import a zipped database, you might see a timeout error because phpMyAdmin takes too long to execute the script.To fix this:

- Set the max_execution_time of `php.ini` to larger value
- Try to import the file again.

Remember to change the ExecTimeLimit setting back to its original value once the import process ends.

#### phpMyAdmin "Error during session...open(SESSION_FILE, O_RDWR) failed: Permission denied"

Cause of the problem: the permission setting of the session. save_path path directory of PHP is incorrect.  
Solution: Using SSH to run the following command  
```shell
chown -R root:nginx /var/lib/php/session
```

#### When restart Nginx service, such error *No spaces...*

Do not worry, the Nginx service is running

#### Nginx 502 error

There are many reasons for the Nginx application server's 502 error, but it is basically caused by insufficient resources. Including: insufficient memory, excessive CPU, full hard disk, there may also be programs that cause php-fpm to stop running. Corresponding solutions:

- The memory and CPU exceed the standard. The three services of php-fpm and nginx mysql can be temporarily solved by restarting. if it is a 1-core 1g configuration and 502 errors often occur, it is recommended to upgrade.
- If the hard disk is full, MySQL will stop serving and need to expand the hard disk
- The php-fpm service stops or the error will also appear 502. php-fpm needs to be restarted.

#### Nginx service restart error

Please make sure the `default.conf` is correct for you, and you can track and analyze log files from */var/log/nginx*