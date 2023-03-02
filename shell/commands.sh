# Getting geometry an position of window:
  xdotool getwindowfocus getwindowgeometry
# or we can select window:
  xdotool selectwindow getwindowgeometry

# multipass
sudo systemctl stop snap.multipass.multipassd.service
sudo vi /var/snap/multipass/common/data/multipassd/multipassd-vm-instances.json
sudo systemctl start snap.multipass.multipassd.service


# QEMU
sudo qemu-img resize vault/instances/poised-surfbird/ubuntu-20.10-server-cloudimg-amd64.img +10G

# if it says that qemu can't resize it because of snapshots:
sudo qemu-img info debian.qcow2
# => image:
# => file format:
# => virtual size:
# => disk size:
# => ...
# => Snapshot list:
# => ID -> 1; TAG -> snapshot1

# to delete taken snapshots from image
sudo qemu-img snapshot -d snapshot1 debian.qcow2


# Get first page of the pdf as png with 300 DPI
# or -r 300 for DPI when x and y resolutions are the same
pdftoppm input.pdf outputname -png -f 1 -singlefile -r 300
pdftoppm input.pdf outputname -png -f 1 -singlefile -rx 300 -ry 300


inotify-tools


rsync --delete --verbose --recursive --update --progress /mnt/hdd/Documents/ /mnt/half/Documents


hey -n 20000 -c 50 http://127.0.0.1:8080


xev | grep button

column -s ":" -t file 
cat file | fzf
xprop

# BPF Compiler Collection
bcc

gdu
  # alternative for ncdu
  https://github.com/dundee/gdu



asdf reshim 'lang_name'
  asdf reshim ruby
