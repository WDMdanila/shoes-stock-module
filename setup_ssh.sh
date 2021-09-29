#!/bin/bash

set -e

docker-compose exec -u root web bash -c 'apt-get update && apt-get install -y ssh rsync && rm -rf /var/lib/apt/lists/*'
docker-compose exec -u root web bash -c "( \
  echo 'LogLevel DEBUG2'; \
  echo 'PermitRootLogin yes'; \
  echo 'PasswordAuthentication yes'; \
  echo 'Subsystem sftp /usr/lib/openssh/sftp-server'; \
) > /etc/ssh/sshd_config_test_clion"
docker-compose exec -u root web bash -c "mkdir /run/sshd"
docker-compose exec -u root web bash -c 'echo "root:password" | chpasswd'

echo "======================================"
echo "Finished setup, restarting compose"
echo "======================================"

bash restart_docker.sh
