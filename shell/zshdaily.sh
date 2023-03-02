Zsh Daily Tips on Twitter Archive


2015-11-19
# Clean up file names and remove special characters
# $1 holds path $2 filename
zmv -n '(**/)(*)' '$1${2//[^A-Za-z0-9._]/_}


2015-11-16,"zmv '(*)' '${(L)1}'  # lowercase file names
zmv 'pic(*).jpg' 'pic${(l:4::0:)1}.jpg' #  pic1.jpg,pic11.jpg to pic0001.jpg,pic0011.jpg (pad 0)


2015-11-13
# zmv regexp memory renaming
autoload -U zmv
zmv '(*).html' '$1.php'
zmv '(*)_(*)' '$1-$2'


2015-11-11
# awkward file names trick
touch ./-Mike.txt
rm -Mike.txt
rm: unknown option -- M
Try 'rm ./-Mike.txt' to remove the file â€?Mike.txtâ€?


2015-11-09
# estring take control of what's listed
print -rl **/*.A(.e_'REPLY=$REPLY:r; [[ -f $REPLY.B ]] ; echo $REPLY.{A,B} '_) > /dev/null


2015-11-05
# splitting PATH variable
for e in ${=PATH//:/ };echo $e
for e in ${(s(:))PATH};echo $e
for e in $path[@];echo $e
for e ($path[@]){echo $e}


2015-11-04
# files not matching 'pattern'
print -rl -- *(.^e{'grep -q pattern $REPLY'})
or
: *(.e{'grep -q pattern $REPLY || print -r -- $REPLY'})


2015-11-03
# count with estring
ls **/*(e:'[[ -e $REPLY/index.php && -e $REPLY/index.html ]]':)
ls **/*(e:'l=($REPLY/index.*(N)); (( $#l >= 2 )) ':)


2015-11-02
# estring
# find c files with more than 10 lines
ls **/*.c(-.e{'((`wc -l < $REPLY` > 10))'})


2015-11-01
# estring qualifer
print **/*.c(e_'[[ -e $REPLY ]]'_)  # neutral just lists
# c files w/o  .o
print **/*.c(e_'[[ ! -e $REPLY:r.o ]]'_)


2015-10-23,"alias -g NL1=' ~1/*~vssver.scc(om[1])' # newest file in previous directory
alias -g NL2=' ~1/*~vssver.scc(om[2])'
cp NL2 .


2015-10-16
# detect if variable exists null value or not
echo ${+PS1} ${+xyq}
1 0
xyq=''
echo ${+PS1} ${+xyq}
1 1
man zshexpn


2015-10-15
# $match
sstring="before inside after"
[[ "$sstring" = (#b)([^i]#inside)(*) ]]
echo $match[1]
echo $match[2]


2015-10-11
# match word beginning
[[ "foo bar" = *([^[:WORD:]]|(#s))bar* ]] && print yes
[[ "obar foo" = *([^[:WORD:]]|(#s))bar* ]] || print no


2015-10-05
# zed simple editor
autoload zed
zed myfile.txt
zed -f myfunc
https://t.co/qUlSHL6Uzl


2015-10-01
# previous directories
setopt autopushd
autoload -U compinit && compinit
echo  ~- ~1 ~2 ~-1 ~-0 ~0
cd -<tab>
cp ~-<tab><tab> ~2<tab>


2015-09-24
# precise dates/times
autoload -U age
ls -tl *.*(e#age 2015/06/01 now#)
ls -tl *(.e#age 2015/06/01 2015/06/30#)


2015-09-11
# latest zsh 5.1
http://t.co/fL349fSlty


2015-09-09
# navigate aliases, functions, history etc
https://t.co/wpKFMx1Ap8


2015-09-02
# oh-my-zsh has 'take' (create subdir and cd to it, here is my attempt
take(){ [ "$#" -eq 1 ] && mkdir "$1" && chdir "$1"}


2015-09-01
# edit command in vi: Esc-v or ALT-V bring up $EDITOR
EDITOR='/bin/vi'
autoload  edit-command-line
bindkey -M vicmd v edit-command-line


2015-08-23,"print *(e*'reply=( this ${REPLY}* )'*)
What problem is this solving?
find out at http://t.co/L7YW0oLDsl


2015-08-19
# clean up file name : generic substitute
setopt extendedglob
file='a b__c_  d.gif'
print ${file//[_ ]##/-}
a-b-c-d.gif # result


2015-08-17,"https://t.co/MyW1x9sxli
grep2awk is a zle function turns the first grep in the
current command line into its awk equivalent,cursor unchanged


2015-08-01,"bindkey -v  # vi cli edit
# eliminate double click of ESC problem where first key stroke ignored
# bind esc to nothing
bindkey -as '\e' ''


2015-07-31
# remote login in with zsh
 ssh  -t root@192.18.001.001 'sh -c "cd /tmp && exec zsh -l"'


2015-07-30
# you need 5.0.8
ps gvim<tab>
# lists just the jobs gvim


2015-07-23,"setopt autopushd
cd -<tab>
alias 1='cd -1'
alias 2='cd -2'
alias 3='cd -3'
alias 4='cd -4'


2015-07-17,"touch {a,a1}.php
ls a1#.php
a.php  a1.php
ls a1##.php
a1.php
X# Zero or more  X
X## One or more  X


2015-07-02,"ls *.php<Ctrl-C>
echo $ZLE_LINE_ABORTED
ls *.php


2015-06-18
# list files that are different on remote server
rsync -rvnc --exclude '*.scc' root@192.168.001.001:${PWD/staging/release}/ .
#  n dryruN


2015-06-14,"useful global aliases
alias -g ...='../..'
alias -g ....='../../..'
alias -g .....='../../../..'
cp 1.php ....
cp ...<TAB>


2015-06-11,"REPORTTIME=5
will automatically report time for any command which lasts longer than 5 secs
info --index-search="reporttime" zsh


2015-06-06
# chpwd is run every time you cd (chdir) use it to change console title etc
where chpwd  # to see what if anything is in yours


2015-06-04
#  hooks (b4 every command precmd if it exists)
> precmd(){echo 'anything you want'}
> date
me/unx/notes/google.md'
Thu, Jun 04, 2015  8:13:38 PM
anything you want


2015-05-29
# movable
scp -rp *(om[1]) root@192.168.168.157:$PWD
# movable & modify path
scp -rp *(om[1]) root@192.168.168.157:${PWD/test/live}


2015-05-20
# upload today's files
scp -p *.php(m0) root@192.129.168.157:/var/www/html/report/


2015-05-15
# get latest file  including possible dot files (D)
ls *~vssver.scc(.om[1]D)


2015-05-11
# my first stab at an aide-memoire of the bits of zsh I use frequently
http://t.co/wZOFoBeq9t


2015-05-09
# exclude directory at any depth e.g. junk
 ls **/fred.jpg~(|*/)junk(|/*)
# e.g. exclude /*junk*/
ls **/fred.jpg~(|*/)*junk*(|/*)


2015-04-29
# you can chain file globs
ls -1 ./(async|inc)/*.php~test.php(om) *.php(om)
for f (./(async|inc)/*.php~test.php(om) *.php(om)) {php -l $f}


2015-04-23
# use variable function name to share script but change behaviour
fun{a,b}(){echo $0}  # create funa funb

fun{0..9}(){echo $0} # fun0-fun9
:x

2015-04-14
# zsh show ambiguity, useful when completing on files with very similar names

http://t.co/VFCMeAHlN7

info --index-search="ambiguity" zsh


2015-04-13
# retrieving a particular parameter from history
ls xx vv hh bucket fred
...
...
vi !?buck?^  # first
echo !?fred?2  # 2nd


2015-04-10
# select 3rd file
ls  xyz*
vi !$([3])


2015-04-09,"info --index-search="zcalc" zsh
autoload zcalc
zcalc '23.0 / 3'
zcalc
PI*2


2015-04-01
# Collection of ZSH frameworks, plugins, tutorials & themes
https://t.co/0wgaqnaMoK


2015-03-30
# file + full path
echo ost-config.php(:a)
/var/www/osticket/upload/include/ost-config.php
# did not explain this tip properly (:a) (all)


2015-03-20
# exclude extensions and exclude directories
ls -1t  report/**/^(vssver.scc|*.js|*.png|*.bak)~*/(async|images)/*(.om[1,20])


2015-03-16
# accessing output of locate (assumes no spaces in file names)
a=($(locate my.cnf))
cd ${a[1]}(:h)
vi ${a[1]}


2015-03-14
# see your directory tree
 ls -d /var/www/html/**/*(/)


2015-03-12,"pathtovim==gvim
echo $pathtovim
/cygdrive/c/VIM/VIM74/gvim


2015-03-11
# DIY zsh write your own functions
# ignore .scc .bak .obj
not(){reply=("$(echo $REPLY |grep -iva '.scc\|.bak\|.obj')")}
ls fred.*(+not)


2015-03-10
# global sed substitute
zargs **/*.(php|inc) -- sed -i 's#ereg_replace("\([^"]*\)"#preg_replace("/\1/"#g'
# preg_replace requires //


2015-03-09
# of course you could also do to get the first match
cd **/note027.txt([1]:h)
# zsh is a bit like lego just bolt another bit on


2015-03-08
# cd to directory containing report.php
cd **/report.php(:h)
# fails if more than 1 report.php


2015-03-06
# access time picks up files that have been "used" ie cat,edit etc
ls -l *(.aM-1)
 the date shown will be confusing so use
 ls -lu *(.aM-1)


2015-03-05,"ls -l *(mh-2)  # modified in past 2 hrs
ls -l *(ch-2)   # changed in past 2 hrs, also picks up files that have been moved/renamed


2015-03-03
# filter by permissions read-write-execute 4-2-1
ls y*(.f777)
ls *.jpg(f644)


2015-03-02
# line continuation
[ -e file1 ] && [ -e file2 ] && echo 'both'
# or
[ -e file1 ] &&
[ -e file2 ] &&
echo 'both exist'
# or
ls ;\
date


2015-02-27,RT @ohmyzsh: Sticker sighting in France. http://t.co/ILqqa7Zpnm


2015-02-27,"zmodload -i zsh/mathfunc
echo $(( pi = 4.0 * atan(1.0) ))
print $(( rand48(seed) ))
echo $(( sin(1/4.0)**2 + cos(1/4.0)**2 - 1 ))


2015-02-25,"filter by ext,exclude dirs,filter by size,date,owner,group,perms
ls -l **/*.(js|php|inc)~(junk|libs)/*(.Lk-2m-14u:nobody:g:apache:xXom[1,3])


2015-02-23
# from http://t.co/lgepDuH7mr
ls -l **/*(.Lm-2mh-1om[1,3])
Lm-2 # <2mbs
mh-1 # less 1 hr
om[1,3] most recent 3


2015-02-20
# list files newer than 22/10/14 from specific directories
autoload -U age
ls [01]<->201[45]/Daily\ report*.csv(e#age 2014/10/22 now#)


2015-02-18,"ls positiveglob~negativeglob(modifiers)
e.g. list all files without an extension ( no dot)
ls *~*.*(.)
ls allfiles except dotfiles filesonly


2015-02-13,"man zshall
# better search the zsh man pages
# e.g.  for bindkey
info --index-search=bindkey zsh
zinfo(){info --index-search="$*" zsh}


2015-02-10
# backup a file with a prefix
cp longfilename.php backup_!#^
cp {,backup_}longfilename.php   # pretty cute


2015-02-09
# backup a file (with a suffix)
cp longfilename.php !#^:r.bak
cp longfilename.{php,bak}   # alternative


2015-02-06,"cp longfilename.php !#^:r.bak
or
cp longfilename.php !#$:r.bak
or
cp longfilename.php !#$:s/php/bak/
# use <tab> to complete, more tomorrow


2015-02-05
# Current line history
!#:0    command
!#^     first
!#1    first
!#1-4  first 4
!#$     last
!#*     all
!#-    all but last


2015-02-04,@hyc_symas @ttyS1  The D operator allows you to include dot files in a glob


2015-02-04
# D is for DOT FILES
ls *(.D)  # include dotfiles
touch .xxx xxx
ls *xxx*(.)
xxx
ls *xxx*(.D)
.xxx xxx


2015-02-02
# precise date filtering
autoload -U age
ls -lt *(.e#age 2014/10/15 2015/01/15#)


2015-02-01
# archiving old files
mv  *(.mM+12) old/     # files older 12 mths
mv *(/mM+12) 2013archive/ # old directories


2015-01-30,"m[Mwhms][-+]n
*(.mh3)  # 3 hrs ago
*(.mh-3) # < 3 hrs
*(.mh+3) # > 3 hrs
*(.^m0) # not today
*(.mw0)  # this week
*(.mM1)  # last month


2015-01-23
# :a modifier display full path
ls *(.:a)


2015-01-22,":e :h :t :r  modifiers
 $f:e is $f file extension
   :h --> head (dirname)
   :t --> tail (basename)
   :r --> rest (extension removed)


2015-01-18
# newest file from previous directory
setopt autopushcd
vi ~1/*(.om[1])


2015-01-16
# ZSH-Lovers  List files in reverse order sorted by name
  $ print -rl -- *(On)
  or
  $ print -rl -- *(^on)


2015-01-11
# Remove zero length and .bak files in a directory
  $ rm -i *(.L0) *.bak(.)


2015-01-09
# All files in /var/ that are not owned by root
$ ls -ld /var/*(^u:root)


2015-01-08
# I will now start randomly tweeting gems from

http://t.co/imT2cMf0wx

echo $[${RANDOM}%1000]


2015-01-03
# mastering $REPLY
# list .c files with no .o
touch {f,j}.{c,o} k.c l.c
print *.c(e_'[[ ! -e $REPLY:r.o ]]'_)
# _ delimits :r strip .c


2014-12-29
# DIYcompletion widgets
gvim ~/.zshrc # gvim needs DOS path so doesn't work
gvim ~/.zshrc(+cyg)
cyg(){reply=("$(cygpath -m $REPLY)")


2014-12-26
# online zsh help
http://t.co/1I706qiJhH
http://t.co/e1zvJKuCUO
http://t.co/736NmOcFe0


2014-12-22
# what's in his dot files

http://t.co/5qwgkTO1RI


2014-12-17,"remember you have completion on man
man zsh<tab>
zsh zshall zshbuiltins  zshcompctl   zshcompwid   zshexpn   zshmodules etc


2014-12-01,"Productivity Tip 14
modifying previous command
r oldstr=newstr
^fred^joe
^str1^str2^:G
^str1^str2^:u:p
!!:gs/fred/joe/


2014-11-25,"Productivity Tip 13
What's been updated?
alias lsnew='ls -lt  **/*(.om[1,10])'
alias lsnew2='ls -lt  **/*(php,inc,js,css)(.om[1,10])'


2014-11-18,"Productivity Tip 12
Search a web root with exclusions
alias zg='zargs **/*.(js|php|css|inc)~(libs|test|temp|wiki|dompdf)/* -- grep -i '


2014-11-15,"Productivity Tip 11
# diff all files in parallel directory
alias diffall='for f (*.php~test.php(.om)) { diff -q $f  ${PWD/html/staging}/$f}'


2014-11-10,"Productivity Tip 10
syntax check all php files in date order
alias phpall='for f (*.php~test.php(om)) {php -l $f} | more'


2014-11-05,"Productivity Tip 9
REL dynamically readjusts to parallel dir
alias -g REL=' ${PWD/html/release}'
diff index.php REL
cd inc
diff main.inc REL


2014-10-31,"Productivity Tip 8
powerful history
Recall just last parameter from history which contains string sql
ls !?sql?$<tab>


2014-10-23,"Productivity Tip 7
jump to any recently visited directory with cd -<tab>
autoload -U compinit && compinit
setopt autopushd
cd  -<tab>


2014-10-16,"Productivity Tip 6
up-line-or-beginning-search
down-line-or-beginning-search
type php then up/down arrow through history of previous php


2014-10-09
# Productivity Tip5 :globals to create meta-lang
alias -g NF='*(.om[1])'  # newest file
alias -g ND='*(/om[1])'  # newest directory
cp NF ND


2014-10-07,"ZSH Productivity Tip 4 the modifiers
cp *.mp3(m0) g:/   # copy today's mp3 only
vi *(om[1])            # edit newest file


2014-10-02
# zsh Productivity Tip 3
# **/* with +ve & -ve filtering .use an alias
grep -i 'fred' ./(junk|colin)/**/*.(php|inc|js)~(**/wiki|**/dompdf)/*


2014-09-26,"ZSH Productivity Tip 2
By binding _expand_alias to the Tab key
I can tab-expand my aliases and modify them as necessary
thus fewer aliases


2014-09-23
# zsh productivity tip 1 named roots
hash -d www='/var/www/html'
hash -d del='/tmp/del'
cd ~www/www.site.com
mv file ~del


2014-09-19,"I'm planning to do a "The/My 10 best features of ZSH"  series of tweets over the next few weeks. Not in any particular order though.


2014-09-15,"Using zsh on cygwin on Windows 8 and having trouble with compinit, compaudit because chown isn't doing anything etc  http://t.co/6OZ3B7pbQs


2014-09-10
# elegance of the for loop
for f (*) mv $f $f.sql
# (.) files only
for f (*(.)) mv $f $f.sql


2014-09-05
# basic zsh filter
ls -1 file*
# select 3rd file in list
vi file*([3])


2014-09-03
# contain keyword
gvim -p $(grep -il 'dunk\|gunk' **/*(.))
gvim -p $(grep -Eil '(dunk|gunk)' **/*(.))
gvim -p $(grep -REil '(dunk|gunk)' .)


2014-08-30
# detailed stats on a file
zmodload -F zsh/stat b:zstat
zstat -g canal-bridge.MOV


2014-08-27
# referring to previous tweet
# complete either end
ls joe<tab>
# completes xxxjoeyyy.txt
# equivalent to
ls *joe*<tab>


2014-08-27,"autoload -U compinit && compinit -i
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' \
    'r:|[._-]=* r:|=*' 'l:|=* r:|=*'


2014-08-25
# try expanding grep !!
grep -<TAB>
# there are 164 different options


2014-08-25
# expand parameters (help)
autoload -U compinit && compinit -i
chmod +<TAB>
X  -- execute
g  -- group
o  -- other'
r  -- read
.. etc


2014-08-22,"servi<TAB>
service htt<TAB>
service httpd res<TAB>
service httpd restart


2014-08-14
# expand alias
autoload compinit && compinit
alias e='echo'
zstyle ':completion:*' completer _expand_alias _expand _complete _ignored
e<tab>


2014-08-13
# man for all the zsh builtins from alias to ztcp

http://t.co/gNf9dfXeGM


2014-08-12,"ls -l *.*(mh-3)   # less than 3 hours
ls -l *(.mh-3)    # . means files only


2014-07-26
# test if a parameter is numeric
if [[ $1 == <-> ]] ; then
echo numeric
else
echo non-numeric
fi


2014-07-21
# copy-earlier-word bound to say control-o
cycles through  each parameter on command line very useful


2014-07-18,"autoload -Uz copy-earlier-word
zle -N copy-earlier-word
bindkey -M viins '^O' copy-earlier-word
cp fred.php old_^O^O #  to old_fred.php


2014-07-16
# one spelling variation
touch bungo bango tango
ls (#a1)bungo
bango  bungo
# two spelling variations
ls (#a2)bungo
bango  bungo  tango


2014-07-13
# glob by owner, permissions, age, file size
# filenames no digits ,uppercase
ls -l **/([^A-Z[:digit:]])##(.u:Guest:f:gu+wx,o+wx:Lk-30mM-1)


2014-07-10
# lets push the boat out a bit further
echo **/*(.Lk-2m-9om[1,9]:t:r:uu:Guest:)


2014-07-10,". files only
Lm-2  Less than 2MB
mh-1 Less than 1 hour old
om sort by newest
[1,3] first 3 only
from http://t.co/lgepDuq4kr


2014-07-09
# explanation tomorrow
ls -l zsh_demo/**/*(.Lm-2mh-1om[1,3])


2014-07-06
# The fignore variable lists suffixes of files to ignore during completion
#  http://t.co/TgsrhUKmIS
fignore=( .o \~ .bak .junk .scc)


2014-07-05
# lets be real picky
autoload -U age
ls -l *(.e#age 2013/10/04:10:15 2013/11/04:10:45#)


2014-07-01
# list by age/date
ls -l *.*(mM4)
autoload -U age
ls -tl *.*(e#age 2014/06/01 now#)
ls -tl *.*(e#age 2014/06/01 2014/06/30#)


2014-06-29
# zsh tips archive
vim http://t.co/vrjqXYSxES


2014-06-25
# expand aliases with tab
autoload -U compinit && compinit
zstyle ':completion:*' completer _expand_alias
bindkey '^t' _expand_alias


2014-06-23
# part 3
bindkey "^[[A" up-line-or-beginning-search
bindkey "^[[B" down-line-or-beginning-search
ls <up> only lists previous ls history


2014-06-23
# part 2
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search


2014-06-23
# part 1 Better history searching with arrow keys
autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search


2014-06-17
# list your functions
# o=order k=keys
print -l ${(ok)functions}


2014-06-12
# % minimum match %% maximum match
v=fredjoejoe
echo ${v%joe*}
echo ${v%%joe*}


2014-06-10
# from today's zsh user group : alter last dot to _
 JUNK=R.E.M.
echo ${JUNK/%./_}
echo ${JUNK/.(#e)/_}
# % & (# e) are end anchors


2014-06-09,"@dailyzshtip So instead of typing
cd somedir
just type
somedir


2014-06-09
# cd without typing cd
setopt auto_cd


2014-06-08
# parameters
p()
{
echo "last ${@[-1]}"
echo "2nd last ${@[-2]}"
}
p a b c d


2014-06-07
# :r remove extension :wr multiple
var=fred.txt
echo ${var:r}
var='fred.txt joe.csv sue.xls'
echo ${var:wr}


2014-06-06,"setopt correct
alias grepp='nocorrect grepp'
unsetopt correct
setopt correctall # spellchecks everything
unsetopt correctall


2014-06-05,"X# Zero or more  X
X## One or more  X
touch {4,44,444,5,45,55,54}.txt .txt
ls 4#.txt
ls 4##.txt


2014-06-01,"^pat Anything that doesnâ€™t match pat
pat1^pat2 Match pat1 then anything other than pat2
pat1~pat2 Anything matching pat1 but not pat2


2014-06-01
# print components of date command
print ${$( date )[2,4]}


2014-05-30
# diff ^ ~
touch {fred,joe}{fred,joe}
ls fred*~*fred*  # never matches
ls fred*~*joe*  # finds fredfred
ls fred^fred # finds fredjoe


2014-05-28
#   # followed by c repeat characters
 touch DATA_6789{00..33}.csv DATA_678988888.csv
ls DATA_[0-9](#c6).csv
ls DATA_[0-9](#c6,).csv


2014-05-24
# repeat command
repeat 3 echo hi


2014-05-22
# eliminate the annoying no match warning for FNG
unsetopt nomatch


2014-05-21
# you can chain ~ filters
touch {a,b,c}{a,b,c} {0,1,2}{1,2,x}
ls *~*c~*b
ls *~b*~c*~<->    # <-> numbers
 ls *~*c~2#       # filter 22 222


2014-05-20
# ^ not in fng
ls x^[3-5]
ls fred^erick*    # list all files fred* except frederick
ls abc^8* ls -lt **/^(vssver.scc|*.ini)(.om[1,10])


2014-05-13,"zsh maths from 'http://t.co/imT2cLGmmt

zmodload zsh/mathfunc
echo $(( pi = 4.0 * atan(1.0) ))


2014-05-10
# ~ with number ranges
touch abc{0..100}.txt
ls abc(<20-100>~<57-67>).txt


2014-05-07
#  how ~ filters
grep -i 'goaty' **/*.{js,php,css} | grep -v 'libs/\|test/\|tmp/'
grep -i 'goaty' **/*.{js,php,css}~*(libs|test|tmp)/*


2014-04-28
# printable zsh reference card
http://t.co/nC7rfzD4Sa


2014-04-24,"autoload -U url-quote-magic && zle -N self-insert url-quote-magic

#  This will auto-quote/escape URLs when typed or pasted


2014-04-23
# games
autoload -U tetris
zle -N tetris
bindkey '^T' tetris


2014-04-21
# zsh tips tweets archive
http://t.co/vrjqXYSxES

http://t.co/l4EUN1Bs5s


2014-04-17
# allow comments on command line
setopt interactivecomments
date # this comment no longer breaks command


2014-04-15
# good stuff
http://t.co/lgepDuq4kr


2014-04-12,"touch -d "4 days ago" x* a* .x .a
ls *(.m4) # 4 days ago
ls *(.m4om[2]) # 2nd file 4 days ago
ls {x,a}*(.m4om[2]D)  # include dot files


2014-04-09
# remember you can dry run a command with echo
# mv all files changed in last hour
echo mv -- *(.ch-1) junk/


2014-04-08,"touch x y .x .y
ll *(m0)    # all files today but gets sub-directories
ll *(.m0)   # only files today
ll *(.m0D) # include dot files


2014-04-06
# separate permissions for files and directories
chmod 755 **/*(/)
chmod 644 **/*(.)


2014-04-01,"http://t.co/YCW5X4V0k4
unit specifiers â€˜Mâ€? â€?â€? â€˜hâ€? â€˜mâ€?or â€?â€?(e.g. â€˜mh5â€? months weeks, hours, mins or secs â€˜dâ€?for days is default.


2014-04-01,@vinc17 Yes interval is a better way of putting it!


2014-03-31,"ls *.*(mh3)  # modified 3 hours ago
ls *.*(mh-3) # less than 3 hours
ls *.*(mh+3) # more tham 3 hours
ls *.*(^mh3) # not 3 hours


2014-03-30,"RT @ashalynd: SQL joins, visualized. http://t.co/yE3TZMhZRc


2014-03-28
# diffing al files in parallel directories /var/www/html/ var/www/test/
alias diffphp='for f (*.php) { diff $f  ${PWD/html/test}/$f}'


2014-03-26
# alternative for loop
# replace every instance of file with new version
for f (**/x) {cp newx $f }
for f in **/x; do;cp newx $f; done


2014-03-24
# alternative ways of cd-ing to deep paths
hash -d dd="/var/www/html/scripts/dd/"
cdpath=(~ /var/www/html/)


2014-03-18
# a simple completer for latex files
zstyle ':completion:*:*:vtex:*' file-patterns '*.tex:tex-files'
function vtex(){gvim $*}
vtex<TAB>


2014-03-16
# multiple redirection
 cat file.txt > file1.txt >> file2.txt > file3.txt


2014-03-13,"textify a phrase to create an image name
s="Fred Goat Dog"
print ${(L)s:gs/ /-/}.jpg
print ${(L)s// /-}.jpg


2014-03-10
# vi mode multiple undo/redo
bindkey -a u undo
bindkey -a '^R' redo
bindkey '^?' backward-delete-char
bindkey '^H' backward-delete-char


2014-03-02
# reply gets each file name
$REPLY:r.o
:r strip extension
.o add .o
[[! -e $REPLY:r.o]]  # does *.o exist
e#''#   execute condition


2014-02-28
# find *.c files which have no *.o
touch  {a,b,c,d}.c {a,c}.o
ls *.c(e#'[[ ! -e $REPLY:r.o ]]'#)


2014-02-27
# test if a file exists before overwriting
[[ -e test/config.php ]] && cp -p test/config.php www/


2014-02-25,"for f (*.php) { php -l  $f }
for i in {11..15} ; ping -n 1 192.18.158.$i


2014-02-24,Hi @mattwoodson !?file0?$ finds a param anywhere in your history not just from previous command. (I lose alt. because I have bindkey -v)


2014-02-22
# please memorise syntax for recalling an individual param
# !?string?0-$
ls file0PGwerlongname.csv
.. other commands
vi !?file0?$<TAB>


2014-02-20
# list  user root files which are not executable
ls -l *.*(u:root:.^x)


2014-02-19
# working with file ownership
# list files not owned by user apache
ls -dl *(^u:apache:)


2014-02-17,"if [[ $1 == <-> ]] ; then
echo parameter is a number
else
echo $1
fi


2014-02-13
# edit/correct previous command :G global :u uppercase :p just display & memory
echo fred
^fred^joe
^joe^& &
^joe^sid^:G
^sid^sue^:G:u:p


2014-02-11,"100th subscriber thanks.
I hope to show that the syntax of zsh is logical
what's been modified today?
ls -lt  /var/www/html/**/*(.om[1,10])


2014-02-10
# attach a command, text etc to a key, use with care
 bindkey -s qq 'ls **/*.php'
# to get code of a function key type cntl-v f5  ^[[15;5~


2014-02-09
# list files younger than 6 hours
ls *.*(mh-6)
# m =modified  h-6 hours - 6
# list files older than 6 hours
ls *.*(mh+6)


2014-02-07
# simple but useful
# copy today's files to a USB
cp *(m0) f:/
cp *.mp3(m0) f:/
# where m0 is m zero


2014-02-04
# Global
zstyle ':completion:*' completer _expand_alias _expand _complete _ignored
vi NF<TAB>
vi *~vssver.scc(.om[1]) <TAB>
vi news.php


2014-02-03
# FNG choices
touch {bb,aa,cc}.{jpg,gif,png}
ls {aa,bb}.(jpg|gif)
ls (*~aa).(*~gif)


2014-01-30
# zsh magic : recall recent directories
setopt autopushd pushdignoredups
cd -<TAB>
cp main.php ~-<TAB>


2014-01-28
# FNG
touch {y,y2}.cfm
ls y2#.cfm y{2,}.cfm y(2|).cfm {y2,y}.cfm (y|y2).cfm y*.cfm


2014-01-26
# renumbering images
autoload zmv
autoload zmv   $ zmv 'pic(*).jpg' 'pic${(l:4::0:)1}.jpg'


2014-01-24
# find all files with no extension
ls *~*.*(.)
# * match all files
# ~*.* except any with a dot
# (.) files only


2014-01-22
# padding left & right
value=314.56
echo ${(l:10::2:)value}
echo ${(r:10::0:)value}


2014-01-21
# num ranges ad nauseum
touch {1..5} {6,7,8,12} {00..03}
ls <-> <-6> <4-> <4-5> 0<-> {1..5} {2,3} {00..03} (4|5) [3-4]  [3-47-8] 0? ?2 *2


2014-01-20
# number ranges
touch x{1..5} {9..6}
ls x<0-5>
ls <->


2014-01-18
# builtin random number $Random
for i in {1..9}; echo $RANDOM


2014-01-17,"cd /v/w/h/<tab>
# expands to
cd /var/www/html/


2014-01-16
# use global alias to replace complex syntax
alias -g REL=' ${PWD/html/release}'
# you must use single quotes here


2014-01-15
# now exclude some directories
zargs ./{html,live}/**/*.{php,inc,js}~(**/wiki|**/dompdf)/* -- tar rvf /tmp/web2$(date "+%d-%m-%Y").tar


2014-01-14
# backup two webroots dev and html
zargs ./{html,dev}/**/*.{php,inc,js} -- tar rvf /tmp/web$(date "+%d-%m-%Y").tar


2014-01-10
# previous tweet saves a command in history that you are not ready to execute
$BUFFER contains command
print -s means print to history


2014-01-07
# ctrl-b save
commit-to-history() {
print -s ${(z)BUFFER}
zle send-break
}
zle -N commit-to-history bindkey "^B" commit-to-history


2014-01-06
# type bindkey to see what  is configured
bindkey
# also set, setopt, mount, alias, autoload, functions, zstyle
# use | more as required


2014-01-03,"zargs ./**/*.{php,inc,js} -- tar rvf /tmp/webbackup$(date "+%d-%m-%Y").tar


2014-01-02
# debug echo shell commands and provide trace info
setopt XTRACE VERBOSE


2013-12-31
# duality of operators :u :l etc
f=FreD
echo ${f:u}
echo FreD
echo !$:u


2013-12-30,"http://t.co/Alky15TAaS
!!:1:s/s1/s2/ Replace string s1 by s2
!!:1:gs/s1/s2/ Same but global
!!:1:& Use same s1 and s2 on new target


2013-12-24,"ls -l *(Lk+100)   # list file size larger/greater than 100kb
 ls **/*(.Lm+10)   # list files larger than 10MB anywhere in hierarchy


2013-12-17
# flip between two deep parallel directories
cd /var/www/html/admin
cd html live > /dev/null &>1 || cd live html > /dev/null &>1


2013-12-16
# just fun but memorise these
touch do re mi
!!:0 !^ !:2 !$ !#$ !#:2 !#1 !#:0


2013-12-15
# lowercase/uppercase all files/directories
zmv '(*)' '${(L)1}' # lowercase
zmv '(*)' '${(U)1}' # uppercase
# the syntax is logical


2013-12-12
# Bulk change the suffix from *.sh to *.pl
zmv -W '*.sh' '*.pl'


2013-12-11
# zmv advanced renaming  , replace spaces by underscore
autoload -U zmv
touch 'filename with spaces.txt'
zmv '* *' '$f:gs/ /_'


2013-12-09
# number ranges
ls fred{09..13}.pl
# list all files fred76.pl to fred88.pl
 ls fred<76-88>.php


2013-12-05
#  cd to deep dirs from anywhere
cdpath=(~ /c/inetpub/wwwroot/  /c/intdoc/)
cd website1
# where website1 is /c/inetpub/wwwroot/website1/


2013-12-04
# start zsh without your usual config (for testing etc)
zsh -f


2013-12-02
# tip part 2
# with previous tweet
ls fred<tab>
# will complete middle of filename e.g. longfred.txt


2013-12-02
# tip part I
autoload -U compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'   'r:|[._-]=* r:|=*' 'l:|=* r:|=*'


2013-12-01
# oh my zsh a project to facilitate configuring zsh
https://t.co/9tUvMIztjt


2013-11-28
# elegant ftp
autoload -U zfinit
zfinit
zfparams http://t.co/FV4p7oNuqI userid password
zfopen
zfput zshtips.html


2013-11-27
# check syntax of PHP files with quote in name
for i in quote_* ; php -l $i


2013-11-25
# recall from current line
cp longfilename.php backup_!#^<TAB>
# here !#^ !#1 !#$ all recall longfilename.php
# also !#0


2013-11-21
# expands to mv textfile.txt textfile.bak
mv textfile.{txt,bak}


2013-11-20
# create a backup copy of a file
cp {,bak_}verylongfilename.tex


2013-11-18
# another way to edit a previous command
!-2:gs/fred/joe/
!?php5?:gs/5/6/


2013-11-15
# newest directory
alias -g ND='*(/om[1])'
# newest file
alias -g NF='*~vssver.scc(.om[1])'
cp NF ND


2013-11-14
# variety
ls *.{jpg,gif,png}
ls *.{jpg,gif,png}(.N)   # does not break if one type missing
ls *.(jpg|gif|png)


2013-11-12
# very good, simply explained
http://t.co/yEFBz3wZu1


2013-11-11,"ls **/*~*/.git/*
# ignore all git subdirectories *~* matches a path


2013-11-07
# copy to a deep parallel directory
cp ${PWD/dev/html}/getRecord.php .
# e.g from /var/www/dev/include/ to /var/www/html/include


2013-11-06
# push current command into a buffer, allows you to do another command then returns to previous command
bindkey '^L' push-line


2013-11-04
# for previous tweet you need, also you can program any key
bindkey -v # vi mode line editting


2013-11-04,"bindkey -M viins '^O'   # copy-prev-shell-word

cp longname.php <control-O> duplicates longname.php which you then modify


2013-11-02
# thanks for first 61 followers & retweets
http://t.co/2qyThaJzdR


2013-11-01,"bindkey '^[[A' history-beginning-search-backward # Up
bindkey '^[[B' history-beginning-search-forward # Down
cd (up recalls prev params)


2013-10-31
# writes ls results to file1 & file2 appends to file3 . multi-io
ls > file1 > file2 >> file3 | wc


2013-10-30
# recall most recent cmd containing string 'client'
!?client<tab>
# recall last parameter of cmd containing 'client'
vi !?client?:$<tab>


2013-10-28
# history substitution
!^      first parameter
!:1-4   first 4 parameters
!$      last parameter
!*      all parameters


2013-10-27
# ^^ correct /alter previous command
cp x2 src/
^2^3
cp x3 src/


2013-10-25
# list 5 most recent files anywhere in hierarchy
ls -lt **/*(D.om[1,5])


2013-10-24,"* all files
~ except for
*.* all files with a dot
(.) files only


2013-10-24
# list all files without an extension ( no dot)
ls *~*.*(.)


2013-10-23
# list pesky empty files (yes that is a zero)
ls *(.L0)


2013-10-22,"autocd is where you just have to type the directory name to "cd" to it.
Are there any drawbacks to autocd?


2013-10-21
# type ... to go back up 2 directory levels
alias ...='cd ../..'


2013-10-20
# .zshrc : access vim scratch files vx1 to vx9
function vx{0..9}(){gvim.exe c:/aax/${0/#v/} &}


2013-10-19
# create shortcuts to deep directories (put in .zshrc)
hash -d www="/var/www/html"
cd ~www


2013-10-18
alias -s php='c:/wamp/php/php.exe'  # now just type test.php to execute it


2013-10-17
newsgroup gmane.comp.shells.zsh.user newsserver http://t.co/33KL177lTf or via web http://t.co/L7YW0p3ejT


2013-10-15
"yum install zsh  # on many linux systems, for cygwin users select zsh from the setup.


2013-10-13
@iSteveMcIntyre Enjoy!


2013-10-13
ls (x*~x[3-5])    # list files x* except x3 to x # thank You Steve Mac my first follower!


2013-10-13
"zargs ./**/*.{php,inc,js} -- tar rvf dev2$(date '+%d-%m-%Y').tar # tar just source files in a directory


2013-10-09
"cd str1 str2 # this will substitute the string "str1" from your directory path and replace  it with "str2".


2013-10-07
"ls -lt  **/*.php(.om[1,20]) # list 20 newest php files anywhere in directory hierarchy


2013-10-03
ls *(m0)   # list all files modified in last 24 hours


2013-10-01
mv *.*(^m-1) archive/ # move all but today's files to sub-directory archive


2013-09-29
vi ~+<tab> 1 /c/aaz 2 /c/aaa 3 /c/aax 4 /usr/bin  # vi a file in recently visited directory


2013-09-29
cd ~<tab>  # display a list of recently visited directories then select the one you wish to return to


2013-09-27
vi **/myfile.txt   edit a file somewhere in hierarchy


2013-09-26
"The elegant way zsh handles recursion. list all files main.php, main.css anywhere in directory / subdirectories >
ls -l **/main.{php,css}
