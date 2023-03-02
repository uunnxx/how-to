# ZSH Tips by ZZapper
# zzappers Tips Home
#
# Updated : 15Mar19 *N* Marks New *C* Corrected/Changed
# zsh -f   # start a "clean" version of zsh (without your startup files .zshrc .zsh*)
# print $ZSH_VERSION
# Tips Home
# Daily ZSH Tip on Twitter  *N*
# ZSH TIPS on Twitter Archive
# http://www.zsh.org/mla/ Searchable Mailing List Archive
# http://grml.org/zsh/zsh-lovers.html
# http://zsh.sourceforge.net/Doc/  Everything? *C*
# Zsh-Reference-Card *C*
# http://zshwiki.org/
# Download latest version (Sourceforge) *N*
# oh my zsh Framework
# zsh IRC Channel: Instant help
# man zsh
# man zshall
#
# zshall       Meta-man page containing all of the above
# zsh          Zsh overview
# zshroadmap   Informal introduction to the manual
# zshmisc      Anything not fitting into the other sections
# zshexpn      Zsh command and parameter expansion
# zshparam     Zsh parameters
# zshoptions   Zsh options
# zshbuiltins  Zsh built-in functions
# zshzle       Zsh command line editing
# zshcompwid   Zsh completion widgets
# zshcompsys   Zsh completion system
# zshcompctl   Zsh completion control
# zshmodules   Zsh loadable modules
# zshcalsys    Zsh built-in calendar functions
# zshtcpsys    Zsh built-in TCP functions
# zshzftpsys   Zsh built-in FTP client
# zshcontrib   Additional zsh functions and utilities
# info --index-search=age zsh         # get man info for zsh function age *N*
# zinfo(){info --index-search=$1 zsh} *N*
#
# /usr/share/zsh/htmldoc/zsh_toc.html
#
# Install on Linux
yum install zsh *N*
yum update zsh *N*
# install from source
cd /tmp
ver=5.7.1
wget https://sourceforge.net/projects/zsh/files/zsh/$ver/zsh-$ver.tar.xz/download
tar xvfJ download
cd zsh-$ver && ./configure && make && sudo make install
# yum install gcc ncurses-devel # if required


# Global aliases
# Searching and filtering my mysql database with my own utility searchdb
# >searchdb client1 | grep -i website1 | fmt -50 | putclip
# How you can simplify this using 3 zsh Global Aliases
# >searchdb client1 G website1 F P
alias -g ND='*(/om[1])' # newest directory
alias -g NF='*(.om[1])' # newest file
# edit newest file in newest directory *N*
VDF(){cd *(/om[1]);F=$(echo *(.om[1]));vi $F}
#Example of use
cp NF ND          # copy newest file to newest directory
cat NF > $(print NF).txt # *N*

# useful zsh stuff *N*
ls *(.)           # list just regular files *N*
ls -d *(/)           # list just directories *C*
ls *(.[3])        # third file *N*
vi *(.om[1])      # vi newest file
cd **/*.php(.om[1]:h) # cd to directory of newest php file *N*
gvim.exe *~vssver.scc(.om[1]) & # newest file ignoring any vssver.scc
vi -p *(.om[1,3]) # open 3 newest files in tabs (gvim)
ls -lt  **/*(.om[1,20]) # list 20 newest files anywhere in directory hierarchy (very useful) *N*
ls -lt  **/*.php(.om[1,20]) # list 20 newest php files anywhere in directory hierarchy (very useful) *N*
grep -i "$1" **/*.{js,php,css}~(libs|temp|tmp|test)/* # exclude directories from grep *N* EXTENDED_GLOB required
ls -lt **/*~*vssver.scc(.om[1,20])  # excluding vssver.scc *N*
ls -lt **/^vssver.scc(.om[1,20])    #  excluding vssver.scc (simpler) *N*
ls -lt **/^(vssver.scc|*.ini)(.om[1,20]) # excluding vssver and any *.ini *N*
ls (../)#junk2/down.txt(:a)   # locate a file "upwards" *N*
vi *(m0)          # re-edit all files changed today!
ls *(^m0)         # files NOT modified today
ls -l *(m4)       # list files modified exactly 4 days ago
ls -l *(.m4)      # list files modified exactly 4 days ago (ignore directories)
vi **/main.php    # where ever it is in hierarchy
ls -l **/main.{php,js,css}    #    *N*
ls *(.)^php~*.c~*.txt   # useful? *N*
ls fred^erick*    # list all files fred* except frederick*    *N*
ls ^*.pdf         # list all but pdf's *NN*
ls  ^httpd.*(.)   # list all but httpd.* in current directory *NN*
ls ^*.(css|php)(.)# list all but css & php #N#
ls x^[3,5]        # list files x* except x3 x5 *N*
ls x*~x[3,5]      # list files x* except x3 x5
ls x*~^x[3,5]     # list only x3 x5
ls **/*~*/.git/*  # ignore all git subdirectories *~* matches a path *N*
vi !$             # vi last parameter
vi !-2:2          # second parameter of second but last command
vi !$:r.php       # vi last parameter but change extension to .php
^php^cfm          # modify previous command (good for correcting spellos)
ls *(.L0)         # list pesky empty files (yes that is a zero) *N*
ls -l *(L-2)      # list file size less than 2 bytes *N*
ls -l *(.L-20)    # list file size less than 20 bytes - . ignore directories *N*
# zsh list largest / biggest files , files larger than
ls -l *(Lk+100)   # list file size larger/greater than 100kb *N*
ls -l *(Lm+2)     # list file size larger/greater than 2 mbs *N*
ls **/*(.Lm+10)   # list files larger than 10MB anywhere in hierarchy *N*
ls -hlS **/*(.Lm+2)  | less  # list largest files  largest first  *N*
ls -hlS /**/*(.OL[1,10]) # find the 10 biggest files on your system *N*
# find 5 largest files in hierarchy with filter by file type & exclude directories
ls -lS **/*.(php|inc)~(libs|locallibs)/*(.OL[1,5]) # *N*
ls *(.m0)  # modified today (last 24 hours)
ls *(.m-1)  # modified today (last 24 hours)
ls *(.^m0)  # not modified today
ls *.*(m3)  # modified 3 days ago
ls *.*(mh3)  # modified 3 hours ago
ls *.*(mh-3) # less than 3 hours
ls *.*(mh+3) # more than 3 hours
ls *.*(^mh3) # all files not 3 hours  old
mv *(.mw+2) old/ # older than 2 weeks *N*
mv *(.mM+6) old/ # older than 6 months *N*
### alias helpers *N*
alias -g OLD='*(.mw+3)' # *N*
alias -g OLDH='*(.mw+3) # m=minutes,d=days(default)w=week,M=Month +n older than n,-n younger than, just n equal to' # *N*
alias -g SIZ ='*(Lk+100)'
alias -g SIZH='*(Lk+100) # L0=zero,Lk kilo,Lm Meg,OL[1,10] 10 largest'
# counts requires extended globbing *N*
setopt EXTENDED_GLOB   # lots of clever stuff requires this
ls DATA_[0-9](#c3).csv  # match all files DATA_nnn.csv  *N*
ls a(#c3).txt     # match aaa.txt   *N*
ls DATA_[0-9](#c4,7).csv  # match DATA_nnnn.csv to DATA_nnnnnnn.txt *N*
ls DATA_[0-9](#c4,).csv  # match DATA_nnnn.csv to DATA_nnnnn.txt etc *N*
ls DATA_[0-9](#c,4).csv  # match DATA_n.csv to DATA_nnn.txt *N*
touch {1..5} {6,7,8,12} {00..03}
ls <-> <-6> <4-> <4-5> 0<-> {1..5} {2,3} {00..03} (4|5) [3-4]  [3-47-8] 0? ?2 *2 # *N*
ls {p..q}<5->{1..4}.(#I)php(.N)  # *N*
touch {y,y2}.cfm
ls y2#.cfm y{2,}.cfm y(2|).cfm {y2,y}.cfm (y|y2).cfm y*.cfm # *N*
touch {t,p}{01..99}.{php,html,c}  # generate 600 test files *N*
#
grep -i "$1" */*.php~libs/*~temp/*~test/* # exclude directories lib,temp,test from grep *N* EXTENDED_GLOB required
# file ownership/permissions
ls -ld *.*(u:apache:)
# excluding files a-m but only if owned by apache
-rwxr-xr-x. 1 nobody (owner) apache (Group) 0 Feb 24 10:23 x.x
ls -l *.*~[a-m]*(u:nobody:g:apache:.xX)
# find all files owned by root (u0), world-writable (W), more than 10k in size (Lk+10) and modified during the last hour (m0)
ls **/*(u0WLk+10m0)
# find all files that don’t have the write permission to group in current directory and all subdirectories
ls **/*(.:g-w:)
# grep
grep -i "$1" **/*.{js,php,css}~(libs|temp|temp|test)/* # exclude directories from grep *N* EXTENDED_GLOB required
grep -iw '$direct' report/**/*.{inc,php}  # searching for a php variable
#  deleting  double dot files & swap files *N*
rm **/.*.swp

# use tab to complete/display history item before executing
!1 # oldest command in your history
!! # previous command
!-2 # command before last
!$ (last argument of previous command)
!$:h (last argument, strip one level)
!$:h:h (last argument, strip two levels)
!?echo
echo !* !!:* (all parameters)
echo !$ !!:$ (last parameter)
echo !^ !:1 !!:1 (first previous parameter)
echo !:2-3   # echo previous parameters 2 to 3 *N*
echo !:2*    # echo previous parameters 2 onwards  *N*
echo !:2-    # echo previous parameters 2 onwards omitting last *N*
echo !:-3    # echo first 3 previous parameters
echo !-2:2 (second parameter of second but last command)
echo convert_csv.php(:a) # echo full path *N*
ls *abc* ;vi !$([3]) # select 3rd file from previous glob *N*

touch 1 2 3    # *N*
!!:0 !^ !:2 !$ !#$ !#:2 !#1 !#0   #  *U*

history               # View recent commands
# history has built-in search (match) *N*
history -m 'yum*'
history -m 'yum*' 0
fc -l  -m 'yum*' 0
!42                   # Re-execute history command 42


# substitute previous command
r oldstr=newstr
!!:s/fred/joe/        # edit previous command replace first fred by joe
!!:s/fred/joe/        # Note : sadly no regexp available with :s///
!!:gs/fred/joe/       # edit previous command replace all fred by joe
mv Licence\ to\ Print\ Money.pdf !#^:gs/\\ //  # rename file removing spaces
^fred^joe             # edit previous command replace fred by joe
^str1^str2^:u:p       # replace str1 by str2 change case and just display
echo chim
^chim^&-&ney-&-&-cheree # reuse LHS
!42:p
also use control-R
^str1^str2^:G         # replace as many as possible

# in all of above remember <TAB> will display changed command WITHOUT executing it *N*

cd !?ls<TAB>   #get command and parameters of a previous ls command
cd !?ls?:*<TAB>   #get (just) parameters of a previous ls command
function scd(){setopt nonomatch;e=/dev/null;cd $1 &> $e||cd ${1}* &> $e||cd *$1 &> $e||cd *${1}* &> $e||echo sorry} *N*
function ddump(){diff -w ~dump/"$1" "$1"}   # *N* diff local file with new one in dump
function cdump(){cp -p ~dump/"$1" "$1"}   # *N* replace local file with new one in dump
# creating generic scripts
function {xyt,xyy} { if [ "$0" = "xyy" ]; then echo run xyy code; else  echo run xyt code; fi ; echo run common code } # *N*


Generating a command from an earlier one
How to recall the parameters of a previous command, on line 7 below
recall the parameters of line 5

5> mv somefile1 /home/saket/stuff/books/
6> acroread somefile.pdf
7> mv somefile2 /home/saket/stuff/books/

> mv !?saket<TAB>
Would bring up the whole line ready for a little editing

or purist

> mv !?saket?:*<tab>
Would just bring up the parameters

If you know the history number of the line (say 5) with desired parameters you can try

> !5:s/somefile1/somefile2/

and if you dont know the history number

!?saket?:s/somefile1/somefile2/

# Variable Substitution *N*
s=(fred joe peter);echo ${s/(#m)*/$MATCH[1,3]} # truncate strings in an array
# History Substitution Summary
#For CURRENT line that you are editing (the # designates current line)
# Remember Tab will expand the following

!#:0    command
!#^     first parameter
!#:1    first parameter
!#:1-4  first 4 parameters
!#$     last parameter
!#*     all parameters
!#$:s/bash/zsh perform substitution on previous parameter

# backup a file with a prefix
cp longfilename.php backup_!#^
cp {,backup_}longfilename.php   # same thing

# backup a file with a suffix
cp longfilename.php !#^:r.bak
cp longfilename.{php,bak}   # expands to cp longfilename.php longfilename.bak


#For Previous Command (for comparison)
!-1     repeat whole command
!!      repeat (shortcut)
!!0     command
!^      first parameter
!:1     first parameter
!:1-4   first 4 parameters
!:-4  !:0-4  first 4 parameters plus command
!!-     all but last parameter *N*
!51$    last parameter of history entry 51 *N*
!$      last parameter
!*      all parameters
!!:s/bash/zsh (or ^bash^zsh)
!^:t    just file name of first parameter
!$:h    just path of last parameter
!-2$:r  just file name without extension of first parameter

For last but one command
!-2     repeat last but one command
!-2^    first parameter last but one command
!-2$    last parameter last but one command
!-2:2   second parameter of second but last command
!-2:s/bash/zsh
etc
For history command 42
!42


!:0 is the previous command name
!^, !:2, !:3, !$ are the arguments
!* is all the arguments
!-2, !-3,  are earlier commands
!-2^, !-2:2, !-2$, !-2* are earlier parameters

ls /                  # recall/step through previous parameters *N*
fred='/bin/path/fred.txt'
echo ${fred:e}
echo ${fred:t}
echo ${fred:r}
echo ${fred:h}
echo ${fred:h:h}
echo ${fred:t:r}
cd !$:h  (remove file name)
# cd to directory containing report.php
cd **/report.php(:h) *N*
cat !!:t (only file name)
# Convert images (foo.gif => foo.jpg):
$ for i in **/*.gif; convert $i $i:r.jpg

# examples of if then else conditionals *N*
[[ 0 = 0 ]] && echo eq || echo neq
[[ 1 = 0 ]] && echo eq || echo neq
if [ $# -gt 0 ];then string=$*;else;string=$(getclip);fi # get parameter OR paste buffer
var=133;if [[ "$var" = <-> ]] ; then echo "$var is numeric" ;fi
if [[ "$ip" = <-> ]] then # check ip address numeric *N*
if [[ "$1" == [0-9] ]]  # if $1 is a digit
if (( $# == 0 ));
if [ $# -gt 0 ]  # parameter cnt > 0 (arguments)
if [[ "$url" = www* ]] # begins with www
if [ "$p1" = "end" ] || [ "$p1" = "-e" ]
if [[ "$p2" == *[a-zA-
