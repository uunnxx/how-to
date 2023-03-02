# Some more stuff to check for
# Check for accidental passwords typed after unsuccessful sudo
cat ~/.bash_history | grep -A5 sudo

# Check for open tmux sessions (possibly logged into root shells)
tmux ls

# Find writable files / dirs outside of your home directory
find / -writable -type f -o -writable -type d 2>/dev/null | grep -Ev "^(/proc|/home/user|/tmp)"

# Check home directories of other users for readable files:
find /home | grep -Ev "^/home/user"

# Find files that were modified in the last 10min (useful to spot funky stuff going on)
find / -mmin -10 2>/dev/null | grep -Ev "^/proc"

# Check mounts
# Grab banners for local ports (using nc or other methods)
# Read crontab job files and look for crappy backup scripts
# Read service configuration (Especially httpd)
# Scroll over ps -ef output and check for passwords passed as command-line arguments
