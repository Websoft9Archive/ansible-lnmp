# 服务启停

使用由 Websoft9 提供的 LNMP 部署方案，可能需要用到的服务如下：

### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

### PHP-FPM
```shell
systemctl start php-fpm
systemctl stop php-fpm
systemctl restart php-fpm
systemctl status php-fpm
```

### MySQL

```shell
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
```

### Redis

```shell
systemctl start redis
systemctl stop redis
systemctl restart redis
systemctl status redis
```

### Tomcat
```shell
sudo systemctl start tomcat
sudo ssystemctl stop tomcat
sudo ssystemctl restart tomcat
sudo ssystemctl status nginx
```