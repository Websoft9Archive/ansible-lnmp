# Parameters

The LEMP deployment package contains a sequence software (referred to as "components") required for LEMP to run. The important information such as the component name, installation directory path, configuration file path, port, version, etc. are listed below.

## Path

### Directories for Application

Suggested directory: */data/wwwroot*  
Example application directory: */data/wwwroot/www.example.com*  

> The URL: *http://Internet IP* will access the example application

### Nginx

Nginx vhost configuration file: */etc/nginx/conf.d/default.conf*    
Nginx main configuration file: */etc/nginx/nginx.conf*   
Nginx logs file: */var/log/nginx*  
Nginx rewrite rules directory: */etc/nginx/conf.d/rewrite*    

**default.conf** includes one [server{}](https://support.websoft9.com/docs/linux/webs-nginx.html#vhost) configuration items whitch matched the **Example application**
```
server
{
listen 80;
server_name www.example.com  example.com;
index index.html index.htm index.php;
root  /data/wwwroot/www.example.com;
error_log /var/log/nginx/example.com-error.log crit;
access_log  /var/log/nginx/example.com-access.log;

include conf.d/extra/*.conf;

## Includes one of your Rewrite rules if you need, examples
 # include conf.d/rewrite/wordpress.conf;
 # include conf.d/rewrite/joomla.conf;
}
```

> How many websites you need, you should add the same number of **server{ }** to **default.conf**

### PHP

PHP configuration file: */etc/php.ini*  
PHP Modules configurations directory: */etc/php.d*
```
# Installed PHP Modules
Core  date  libxml  openssl  pcre  zlib  filter  hash  Reflection  SPL  session  standard    
bcmath  bz2  calendar  ctype  curl  dom  mbstring  fileinfo  ftp  gd  gettext  gmp  iconv  
imap  intl  json  ldap  exif  mcrypt  mysqlnd  odbc  PDO  Phar  posix  recode  shmop  
SimpleXML  snmp  soap  sockets  sqlite3  sysvmsg  sysvsem  sysvshm  tokenizer  xml  xmlwriter  xsl  mysqli  
pdo_dblib  pdo_mysql  PDO_ODBC  pdo_sqlite  wddx  xmlreader  xmlrpc  igbinary  imagick  zip  redis  Zend OPcache  
```

### MYSQL

MySQL installation directory: */usr/local/mysql*  
MySQL data directory: */data/mysql*  
MySQL configuration file: */etc/my.cnf*    
MySQL Web Management URL: *http://Internet IP/9panel*, get credential from [Username and Password](/stack-accounts.md)

### phpMyAdmin

phpMyAdmin installation directory: */data/apps/phpmyadmin*  
phpMyAdmin configuration file: */data/apps/phpmyadmin/config.inc.php*   
phpMyAdmin configuration file: */etc/nginx/conf.d/phpmyAdmin.conf*

### Redis

Redis configuration file: */etc/redis.conf*  
Redis data directory: */var/lib/redis*  
Redis logs file: */var/log/redis/redis.log*


## Ports

You can control(open or shut down) ports by **[Security Group Setting](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** of your Cloud Server whether the port can be accessed from Internet.

These ports should be opened for this application:

| Name | Number | Use |  Necessity |
| --- | --- | --- | --- |
| MySQL | 3306 | Remote connect MySQL | Optional |
| HTTP | 80 | HTTP requests for LEMP | Required |
| HTTPS | 443 | HTTPS requests LEMP | Optional |

## Version

You can see the version from product page of Marketplace. However, after being deployed to your server, the components will be automatically updated, resulting in a certain change in the version number. Therefore, the exact version number should be viewed by running the command on the server:

```shell
# Linux Version
lsb_release -a

# PHP Version
php -v

# List Installed PHP Modules
php -m

# Nginx version
nginx -v

# List Installed Nginx Modules
nginx -V

# MySQL version
mysql -V

# Redis version
redis-server -v
```