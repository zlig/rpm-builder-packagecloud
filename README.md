# rpm-builder-packagecloud
![build](https://github.com/zlig/rpm-builder-packagecloud/actions/workflows/main.yml/badge.svg)

## Overview

Build Red Hat / CentOS .rpm packages (using GitHub Actions) and upload to PackageCloud

## Repository

The artifacts from this project are uploaded as samples in the following Package Cloud repository: [rpms](https://packagecloud.io/geldtech/rpms)

## Usage


### Quick instructions

Add repository to the list of available sources

```
curl -s https://packagecloud.io/install/repositories/geldtech/rpms/script.rpm.sh | sudo bash
```

### Manual instructions

Install pre-requisites

```
sudo yum install pygpgme yum-utils
```

Add manually the repository to the list of available sources

```
echo """
[geldtech_rpms]
name=geldtech_rpms
baseurl=https://packagecloud.io/geldtech/rpms/el/6/$basearch
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/geldtech/rpms/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
""" | sudo tee -a /etc/yum.repos.d/geldtech_rpms.repo
```

### Install package

```
sudo yum install  rpm-builder-packagecloud
```
