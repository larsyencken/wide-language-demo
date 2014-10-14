#!/bin/bash

set -e

# move to using an ubuntu user rather than root
function has_ubuntu_user() {
  grep -q ubuntu /etc/passwd
}

function make_ubuntu_user() {
  adduser ubuntu
  adduser ubuntu sudo
  echo 'ubuntu    ALL=NOPASSWD: ALL' >/etc/sudoers.d/ubuntu
}

function has_exec() {
  /usr/bin/which -s "$1"
}

has_ubuntu_user || make_ubuntu_user

apt-get update
has_exec git || apt-get install -y git
has_exec pip || apt-get install -y python-dev python-pip build-essential python-virtualenv

su - ubuntu <<EOF

test -d wide-language-demo || git checkout --recursive https://github.com/larsyencken/wide-language-demo
cd wide-language-demo
make bootstrap
EOF
