# So, you have a shell on a Linux machine. But what now? Privilege Escalation! (Unless you spawned a root shell
# of course! Then its time for some lateral movement I suppose). But before you can escalate your privileges,
# you will have to figure out how you are going to do it. So that brings us to enumeration,
# which is hands down the most important part of compromising a target.

# So this post is not intended to be a definitive guide to Linux priv-esc or anything, but merely a simple collection
# of things that I have personally found helpful during enumeration. I am totally open to suggestions or any ideas.

# Get Your Bearings:
# First things first. Always get a good feel for the machine.
# Its always a good idea to figure out what version you’re looking at:

cat /etc/issue
# or
cat /etc/*-release

# What is the kernel version? Are there known exploits for that version?
cat /proc/version
uname -a
rpm -q kernel

# Where are you on the network? What connections are established?
ifconfig -a
netstat -antup
iptables -L
arp -e

# What is running?
# There are numerous local privilege escalation exploits out there in the void. Are there any vulnerable applications or services running that have known exploits?
# Which services are being run with root privileges?

ps -ef | grep root
# or
ps aux | grep root
cat /etc/services

# Any vulnerable applications?
ls -alh /usr/bin/
ls -alh /sbin/

# Any files with SUID/SGID permissions?
find / -perm -g=s -o -perm -u=s -type f 2>/dev/null
# or, for a faster search in “bin” directories
for i in `locate -r "bin$"`; do find $i \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null; done


# Uploading and running exploit code
# If there is a local privilege escalation exploit available, how will you upload and execute the exploit code on your target?
# What languages are supported on the machine?
find / -name 'language'
ex: find / -name python*

# Is GCC present?
find / -name gcc

# How can you upload the exploit code? Use find to look for things like:
# wget, nc, netcat, tftp, ftp, fetch etc.
# Where can you write and execute files?
# You will need to find a place to compile and execute your exploit code
# This will locate world writeable and world executable folders

find /\(-perm -o w -perm -o x\) -type d 2>/dev/null


# Cracking password hashes

# Can you view /etc/passwd and /etc/shadow ?
cat /etc/passwd
cat /etc/shadow
# If you can, try to crack the hashes you find. You never know!
# Limited Shell?
# Give these a shot.

python -c 'import pty;pty.spawn("/bin/bash")'
echo os.system('/bin/bash')

# The simplest things are often overlooked
# If I am ever stuck getting root privileges, its 9 times out of 10 because I am overthinking it.
# Sometimes the answer is so simple that its easy to overlook it. If you’re getting stuck,
# think back to square one and move forward slowly and pay attention to the details.
# Here are some of simple things that can be overlooked:
# Is the account you are using a sudoer? If you have the password for the account, you may be able to use sudo.
# I have seen many people look over this. Are there other users that are sudoers?

cat /etc/sudoers
sudo -l

# Always check for password reuse. Unless of course you don’t want to be noisy and risk a failed authentication.
# Sometimes people don’t think straight and put plain text passwords in .txt files and spreadsheets and
# all kinds of terribly insecure places, so don’t disregard the idea.
# Enumeration scripts
# To make life easier, you can write your own bash script to run whatever commands you want, although sometimes
# it is not plausible to do so. For example if you do not have the ability to upload files or execute shell scripts.
# Anyways, those are my usual go-to commands when I start enumerating for priv-esc. It is not an exhaustive
# list by any means, there is a whole world of possibilities out there for getting root and hopefully this will help!
# I’m sure I will add things as I think of them, seeing as I wrote this on my lunch at work and probably
# forgot a bunch of stuff. Happy Hunting.


