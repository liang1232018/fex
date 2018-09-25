#!/usr/bin/env bash
set +e
cd ${DATA_PATH}/
apt-get install -y libevent-dev
apt-get update -y

# below are installation instructions for libmemcached & memaslap client (install on client machine)

# download
wget https://launchpad.net/libmemcached/1.0/1.0.16/+download/libmemcached-1.0.16.tar.gz
tar xf libmemcached-1.0.16.tar.gz
cd libmemcached-1.0.16

# build
CFLAGS=-pthread LDFLAGS=-pthread LIBS=-levent ./configure --enable-memaslap
sed -i "s/#am__append_42 = clients\/memaslap/am__append_42 = clients\/memaslap/g" Makefile
sed -i "s/#am__EXEEXT_2 = clients\/memaslap/am__EXEEXT_2 = clients\/memaslap/g" Makefile
make

# install
make install

cd -
set -e
