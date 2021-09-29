#!/bin/bash

set -e

docker-compose restart
docker-compose exec -d -u root web /usr/sbin/sshd -D -e -f /etc/ssh/sshd_config_test_clion