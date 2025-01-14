#!/bin/sh
#
# This file is part of Celestial (https://github.com/OpenFogStack/celestial).
# Copyright (c) 2024 Tobias Pfandzelter, The OpenFogStack Team.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

# install dependencies
apk -X "http://dl-5.alpinelinux.org/alpine/latest-stable/main" -U --allow-untrusted --root / --initdb add \
    openrc \
    ca-certificates \
    alpine-base \
    util-linux \
    iptables \
    iproute2 \
    strace \
    attr \
    grep \
    chrony

# link rc services
ln -sf /etc/init.d/devfs        /etc/runlevels/boot/devfs
ln -sf /etc/init.d/procfs       /etc/runlevels/boot/procfs
ln -sf /etc/init.d/sysfs        /etc/runlevels/boot/sysfs

ln -sf networking               /etc/init.d/net.eth0
ln -sf /etc/init.d/networking   /etc/runlevels/default/networking
ln -sf /etc/init.d/net.eth0     /etc/runlevels/default/net.eth0

ln -sf /etc/init.d/chronyd      /etc/runlevels/default/chronyd

# disable modules
echo rc_want="!modules">> /etc/rc.conf

# setup chrony to use PTP as the time source
echo "refclock PHC /dev/ptp0 poll -2 dpoll -2 offset 0 trust prefer" > /etc/chrony/chrony.conf

passwd root -d root
exit
