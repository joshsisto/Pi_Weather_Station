#!/bin/bash

VAR_TIME=$(date +%F_%H:%M:%S:%N | sed 's/\(:[0-9][0-9]\)[0-9]*$/\1/')

cp /var/log/user.log /media/2TB/mikrotik/${VAR_TIME}_mikrotik.log
