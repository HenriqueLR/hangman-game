#!/bin/bash -xe

groupadd supersudo && echo "%supersudo ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/supersudo
adduser --disabled-password --gecos hangman hangman && usermod -a -G supersudo hangman && mkdir -p /home/hangman/.ssh
echo -e "Host github.com\n\tStrictHostKeyChecking no\n" > /home/hangman/.ssh/config
sudo chown -R hangman:hangman /home/hangman
sudo chmod 600 /home/hangman/.ssh/*
