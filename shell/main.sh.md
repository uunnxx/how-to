printf "now - %d days\n" {1..332044}  | date -f- +%Y%_m%_d%'\n'%Y%m%d | tr -d ' ' > alldates.txt; rev alldates.txt > revdates.txt; paste alldates.txt revdates.txt | awk '$1==$2{print $1}'


