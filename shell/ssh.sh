# check github page
# ssh-keygen -t rsa

cat ~/.ssh/id_ed25519.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'

# Enable ssh server on Ubuntu 20 04

sudo apt update
sudo apt install openssh-server

# to check if ssh running
sudo systemctl status ssh

# Ubuntu ships with a firewall configuration tool called UFW.
# If the firewall is enabled on your system, make sure to open the SSH port:
sudo ufw allow ssh

# Connecting to the SSH Server
ssh user@hostname

# check hostname with `ip a`


# Disabling SSH on Ubuntu
sudo systemctl disable --now ssh

# re-enable
sudo systemctl enable --now ssh
