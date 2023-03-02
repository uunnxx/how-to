# I always start with a slow, SYN scan using nmap (ping disabled). I usually enable service detection to the max
# (also OS detection). Also, I always write the output to a text file so I can read it anytime without having
# to scan more than once. If the first scan yields somethings interesting,
# I might scan again with one of the NSE scripts enabled.
#
# It's a semi-stealthy, very efficient scanning method.
# The usual command:

nmap -Pn -sS -sV -O -T 2 [TARGET IP] -p1-65535 > nmap.txt
