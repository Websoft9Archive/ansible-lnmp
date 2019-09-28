# Deploy a PHP application

To deploy PHP application on LEMP, you need to add **server{ }** for it

Overall, just need two steps: 
1. Upload source codes of applicaiton
2. Add new VirtualHost in the file [Nginx vhost configuration file](/stack-components.md#nginx) 

> **server{ }** is vhost configuration segment. Each application must correspond to a unique **server{ }** in **default.conf**.

## Prepare

To deploy PHP application on LEMP, you need to know the followings:

*  **Vhost Configuration File**: */etc/nginx/conf.d/default.conf* 
*  **Tools**: Using WinSCP to mange files and run command
*  **Domain Name**: If you want to use Domain you must complete the Domain revolution before
*  **Database**: If the database can't be created automatically during the installation process, please use [phpMyAdmin](/admin-mysql.md) to manage it

Once you have a overall, you can start you application deployment now

## Deploy fisrt application

There is a example application in LEMP, we sugget you to **replace the example application** for deploy first application:

1. Use WinSCP to connect Cloud Server,
2. Delete all files in the folder */data/wwwroot/www.example.com*, but don't delete *www.example.com*
3. Upload your application's codes to the folder: */data/wwwroot/www.example.com* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-uploadcodestoexample-websoft9.png)
4. Modify the  `server{...}` segment ([refer to](/solution-deployment.md#server)) in the file *default.conf* if you want to bind domain or modify folder name
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lamp/lamp-editvhostconf-websoft9.png)
   ::: warning
   If you do not bind the domain and do not modify the directory name, skip steps 4 and 5.
   :::
5. Save the file *default.conf* and then Restart Nginx Service
   ~~~
   sudo systemctl restart nginx
   ~~~
6. Using the Chrome or Firefox to visit: *http://domain* or *http://IP/mysite2* to visit your application

## Deploy second application

Start to deploy the second application, you should add new `server{...}` segment to *default.conf* 

1. Connect Cloud Server, then create a new folder named "mysite2" to the directory */data/wwwroot*
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lamp/lamp-createmysite2-websoft9.png)
2. Upload your application's codes to the folder: */data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lamp/lamp-uploadcodes-websoft9.png)
3. Edite the file *default.conf*
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lamp/lamp-editvhostconf-websoft9.png)

    Have domain or no domain, Choose one of the options below:

     * **Have domain, you can visit application by *http://domain/***  

     Please copy the **server{ }** below to *default.conf*, and modify the **server_name, root, error_log, access_log** and so on ([refer to](/solution-deployment.md#server))
     
       ```
       server
       {
        listen 80;
        server_name mysite2.yourdomain.com;
        index index.html index.htm index.php;
        root  /data/wwwroot/mysite2;
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        include conf.d/extra/*.conf;

        ## Includes one of your Rewrite rules if you need, examples
        # include conf.d/rewrite/wordpress.conf;
        # include conf.d/rewrite/joomla.conf;
        }
        ```

     * **No domain, you can visit application by *http://mysite1.yourdomain.com/mysite2***  
    
     Please copy the **Alias template** below to *default.conf*, and modify the **/path, Directory**

      ```
      location /mysite2
      {
       alias /data/wwwroot/mysite2;
       index index.php index.html;
       location ~ ^/mysite2/.+\.php$ {
        alias /data/wwwroot/mysite2;
        fastcgi_pass  unix:/dev/shm/php-fpm-default.sock;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME /data/wwwroot/$fastcgi_script_name;
        include        fastcgi_params; }
      include conf.d/extra/*.conf;
      }
      ```
      ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/lnmp-insertalias-websoft9.png)

4. Save the file *default.conf* and then Restart Nginx Service
      ~~~
      systemctl restart nginx
      ~~~
5.  Using the Chrome or Firefox to visit: *http://domain* or *http://mysite1.yourdomain.com/mysite2* to visit your application


## Deploy more application

**Deploy more application** is the same with **Deploy second application**

Finally, we know the new and summarize the steps of the LEMP deployment site: 

1. Upload the website code 
2. Dmain name resolution(not necessary) 
3. Add the site configuration or modify the sample site configuration 
4. Increase the database corresponding to the site (not necessary) 
5. Enter the installation wizard

## Server

All items in the **server{}** must be correct, any error may cause Nginx can't start and applicaiton not accessible

|  Server Item  |  Use  |  Necessity |
| --- | --- | --- |
|  server_name  |  domain name, if you configure two domain names, separate them with spaces.   |  Required |
|  root |  The real website storage directory  | Required and must be correct |
|  error_log  | error logs directory   |  Suggestion |
|  access_log  | visit logs directory  |  Suggestion |
|  ssl_certificate  | HTTPS certificate directory   |  Required when using HTTPS |
|  ssl_certificate_key  | HTTPS certificate key directory   |  Required when using HTTPS |

## Q&A

#### Visit my application, dispaly "no permission..." error?

Run the this command
~~~
chown -R nginx.nginx /data/wwwroot
~~~

#### I can't restart Nginx service after modify the *default.conf*?

Check the application directory items in the segement of your *server{ }*

#### I can't visit my new deployment and all applications on my Server 

Check the application directory items in the segement of your *server{ }*

#### 404 error?

Please make sure that the *index.php* or *index.html* was included in the your application's direcotory

#### 500 Internal Server Error？

The program code is wrong, you need to analyze the program's log file.