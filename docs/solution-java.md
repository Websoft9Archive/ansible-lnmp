# Extend Java

If you are using the Java+PHP Image, you can deploy java application directly. Otherwise, you should install Java and Tomcat first. Just one command, you can intall Java and Tomcat on LNMP. 
```shell
yum install tomcat-* -y && systemctl enable tomcat && systemctl start tomcat
```

Using your local Chrome or Firefox to visit java sample applications: [http://Internet IP:8080/sample/]()

---

To deploy a java application in LNMP+Java, you need to know the following six points:

- **Vhost Configuration File:** */etc/tomcat/server.xml*
- **Sites Directory:** */var/lib/tomcat/webapps*
- **Management Tool:** Please using WinSCP which can manage files and run command
- **Domain Management:** Please visit Domain Name to start the installation wizard of site after the revolution of Domain if you want to use Domain for your site
- **Database:** If the database cannot be created automatically during the installation process, please use phpMyAdmin to create the database.
- **Mapping relations:** Each site must correspond to a unique virtual host configuration segment in configuration file `server.xml`

> The details of deploying a website or multiple websites, with or without domain names, are slightly different.

#### WAR package installation sample 

1. Download [jspMyAdmin war package](https://sourceforge.net/projects/japmyadmin2-0/files/latest/download)
1. Using SFTP to upload your code to the directory: _/var/lib/tomcat/webapps_
1. Visit the URL *http://Internet IP:8080/jspmyadmin**  on your local computer,you can access to JspMyAdmin now
1. If you want to bidding Domain Name, set proxy_pass in the Nginx configuration

#### Java application responds very slowly?

You may found that the whether a sample or application your installed, the response is very slow. What is the reason? How to solve?

Why? Java have a class named [SecureRandom](https://docs.oracle.com/javase/8/docs/api/java/security/SecureRandom.html), This class provides a cryptographically strong random number generator (RNG), it may cause JVM wait for more time but this class is not useful in Linux

How? Set recurerandom.source to "file:/dev/./urandom" in the file java.security<br />path: /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.201.b09-2.el7_6.x86_64/jre/lib/security/java.security

```
#1 find this line below
securerandom.source=file:/dev/random

#2 after edited
securerandom.source=file:/dev/./urandom

#3 restart tomcat
systemctl restart tomcat
```