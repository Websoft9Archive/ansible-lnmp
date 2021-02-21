# LNMP Cloud Installer

![](https://libs.websoft9.com/common/websott9-cloud-installer.png) 

## Introduction

[English](/README.md) | [简体中文](/README-zh.md)  

**LNMP Cloud Installer**, developed by [Websoft9](https://www.websoft9.com), is an automatic installation program of **LNMP (Linux-Nginx-MySQL-PHP)** based on Ansible and shell. It helps user install LNMP and pre-configure required items automatically and users only need to run a command on Linux. It simplifies the complicated installation and initialization process.  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)

## System Requirement

System Requirement to install this repository are as following：

| Conditions       | Details                               | Notes                |
| ------------------- | --------------------------------| -------------------- |
| Operating System   | CentOS7.x, Amazon Linux2 | Optional                 |
| Public Cloud     | AWS, Azure, Alibaba Cloud, HUAWEI ClOUD, Tencent Cloud    | Optional                 |
| Private Cloud     | KVM, VMware, VirtualBox, OpenStack    | Optional                 |
| Server Configuration | vCPU no less than 1 core, Memory no less than  1 GIB, Storage no less than 10 GB, Bandwidth no less than 100M ||

## Ecosystem

Core components of this repository: Nginx, PHP 5.6/7.0/7.1/7.2/7.3/7.4, MySQL5.5/5.6/5.7/8.0, phpMyAdmin on docker

Learn more about [Parameters](/docs/stack-components.md).

## Installation

You can install it by thi Cloud Installer solution all in one. In addition, you can deploy image published on major Cloud Platform by Websoft9.

#### All-in-one Installer

Run the automatic installation script with **root** authority to start the installation. If necessary, users need to make interactive choices, and then wait patiently until the installation is successful.

```
$ sudo su -
$ wget -N https://raw.githubusercontent.com/Websoft9/ansible-linux/main/scripts/install.sh; bash install.sh -r lnmp
```

If the network is broken or blocked, SSH will be interrupted and the installation will fail. Please reinstall.

#### Image on Cloud 

Follow our [LNMP image](https://apps.websoft9.com/lnmp) for installation on major Cloud Platform.

## Documentation

**LNMP Administrator Guide** ([English](https://support.websoft9.com/docs/lnmp) | [简体中文](https://support.websoft9.com/docs/lnmp/zh)) includes Getting Started, Password and Best Practices for you

## Changelog

Detailed changes are documented in the [CHANGELOG](/CHANGELOG.md).

## License

[LGPL-3.0](/License.md), Additional Terms: It is not allowed to publish free or paid image based on this repository in any Cloud platform's Marketplace.

Copyright (c) 2016-present, Websoft9

This program provided by Websoft9 contains a series of software with separate copyright notices and license terms. Your use of the source code for the software included is subject to the terms and conditions of its own license.

## FAQ

#### Can I run this repository on Ansible Tower? 

Yes.

#### Is the default password safe?

The solution used the random password solution, every deployment produce unique password which is different from other users
