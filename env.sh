#!/bin/bash

export PATH=$PATH:/usr/lib/openmpi/bin

yum -y install openmpi openmpi-devel glibc-devel.i686 openmpi-x86_64 openmpi-devel.i686
yum group install "Development Tools" -y
yum install glibc-static -y
