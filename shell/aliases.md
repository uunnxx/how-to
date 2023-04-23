| alias                                                                                                                                                                                                                                                                                  | aliased to                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| - | 'cd -'                                       |
| ... | ../..                                      |
| .... | ../../..                                  |
| ..... | ../../../..                              |
| ...... | ../../../../..                          |
| 1 | 'cd -1'                                      |
| 2 | 'cd -2'                                      |
| 3 | 'cd -3'                                      |
| 4 | 'cd -4'                                      |
| 5 | 'cd -5'                                      |
| 6 | 'cd -6'                                      |
| 7 | 'cd -7'                                      |
| 8 | 'cd -8'                                      |
| 9 | 'cd -9'                                      |
| :q | exit                                        |
| B | fzf_books                                    |
| D | 'cd /mnt/hdd/Documents/Books'                |
| DD | 'cd /mnt/hdd/Documents/'                    |
| O | 'xdg-open &>/dev/null'                       |
| _ | sudo                                         |
| __ | 'sudo $(fc -ln -1)'                         |
| aoeu | asdf                                      |
| b | 'bb pdf djvu'                                |
| bat|'bat --theme base16 --color=auto'            |
| batp|'bat --plain --theme base16 --color=auto'   |
| batv|'fzf --preview '\''bat --theme base16 {}'\' |
| bonsai|'cbonsai -ilL60'                          |
| ch|'tldr $(tldr -l \| fzf)' |
| cr|crystal                           |
| cri|'crystal init'           |
| ctl|systemctl                |
| da | 'date '\''+%A, %B %d, %Y [%T]'\'            |
| dbl | 'docker build'                             |
| dcin | 'docker container inspect'                |
| dcls | 'docker container ls'                     |
| dclsa | 'docker container ls -a'                 |
| df | 'df -h'                                     |
| dib | 'docker image build'                       |
| dii | 'docker image inspect'                     |
| dils | 'docker image ls'                         |
| dipu | 'docker image push'                       |
| dirm | 'docker image rm'                         |
| disas | 'objdump -drwCS -Mintel'                 |
| dit | 'docker image tag'                         |
| dlo | 'docker container logs'                    |
| dnc | 'docker network create'                    |
| dncn | 'docker network connect'                  |
| dndcn | 'docker network disconnect'              |
| dni | 'docker network inspect'                   |
| dnls | 'docker network ls'                       |
| dnrm | 'docker network rm'                       |
| dpo | 'docker container port'                    |
| dpu | 'docker pull'                              |
| dr | 'docker container run'                      |
| drit | 'docker container run -it'                |
| drm | 'docker container rm'                      |
| 'drm!' | 'docker container rm -f'                |
| drs | 'docker container restart'                 |
| dst | 'docker container start'                   |
| dsta | 'docker stop $(docker ps -q)'             |
| dstp | 'docker container stop'                   |
| dtop | 'docker top'                              |
| du | 'du -c -h'                                  |

| duu='du --max-depth=1'

| dvi='docker volume inspect'
| dvls='docker volume ls'
| dvprune='docker volume prune'
| dxc='docker container exec'
| dxcit='docker container exec -it'
| editalias='nvim ~/.aliases.zsh'
| editomz='nvim ~/.oh-my-zsh'
| editshell='nvim ~/.zshrc'

| egrep='grep -E --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn,.idea,.tox}'
| fd=fdfind
| fgrep='grep -F --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn,.idea,.tox}'
| fos=fossil
| fuck='TF_CMD=$(TF_ALIAS=fuck PYTHONIOENCODING=utf-8 TF_SHELL_ALIASES=$(alias) thefuck $(fc -ln -1 \| tail -n 1)) && eval $TF_CMD && print -s $TF_CMD'

| g=git
| ga='git add'
| gaa='git add --all'
| gam='git am'
| gama='git am --abort'
| gamc='git am --continue'
| gams='git am --skip'
| gamscp='git am --show-current-patch'
| gap='git apply'
| gapa='git add --patch'
| gapt='git apply --3way'
| gau='git add --update'
| gav='git add --verbose'
| gb='git branch'
| gbD='git branch --delete --force'
| gba='git branch --all'
| gbd='git branch --delete'
| gbda='git branch --no-color --merged \| command grep -vE "^([+*] \| \s*($(git_main_branch) \| $(git_develop_branch))\s*$)" \| command xargs git branch --delete 2>/dev/null'
| gbg='git branch -vv \| grep ": gone\]"'

| gbgD='local res=$(gbg \| awk '\''{print $1}'\'') && [[ $res ]] && echo $res \| xargs git branch -D'
| gbgd='local res=$(gbg \| awk '\''{print $1}'\'') && [[ $res ]] && echo $res \| xargs git branch -d'

| gbl='git blame -b -w'
| gbnm='git branch --no-merged'
| gbr='git branch --remote'
| gbs='git bisect'
| gbsb='git bisect bad'
| gbsg='git bisect good'
| gbsr='git bisect reset'
| gbss='git bisect start'
| gc='git commit --verbose'
| 'gc!'='git commit --verbose --amend'
| gca='git commit --verbose --all'
| 'gca!'='git commit --verbose --all --amend'
| gcam='git commit --all --message'
| 'gcan!'='git commit --verbose --all --no-edit --amend'
| 'gcans!'='git commit --verbose --all --signoff --no-edit --amend'
| gcas='git commit --all --signoff'
| gcasm='git commit --all --signoff --message'
| gcb='git checkout -b'
| gcd='git checkout $(git_develop_branch)'

| gcdeb='gcc -g -fverbose-asm -masm=intel -S'

| gcf='git config --list'
| gcl='git clone --recurse-submodules'
| gclean='git clean --interactive -d'
| gcm='git checkout $(git_main_branch)'
| gcmsg='git commit --message'
| 'gcn!'='git commit --verbose --no-edit --amend'
| gco='git checkout'
| gcor='git checkout --recurse-submodules'
| gcount='git shortlog --summary --numbered'
| gcp='git cherry-pick'
| gcpa='git cherry-pick --abort'
| gcpc='git cherry-pick --continue'
| gcs='git commit --gpg-sign'
| gcsm='git commit --signoff --message'
| gcss='git commit --gpg-sign --signoff'
| gcssm='git commit --gpg-sign --signoff --message'
| gd='git diff'
| gdca='git diff --cached'

| gdct='git describe --tags $(git rev-list --tags --max-count=1)'
| gdcw='git diff --cached --word-diff'
| gds='git diff --staged'
| gdt='git diff-tree --no-commit-id --name-only -r'
| gdup='git diff @{upstream}'
| gdw='git diff --word-diff'
| geca='gem cert --add'
| gecb='gem cert --build'
| geclup='gem cleanup -n'
| gecr='gem cert --remove'
| gegi='gem generate_index'
| geh='gem help'
| gei='gem info'
| geiall='gem info --all'
| gein='gem install'
| gel='gem lock'
| geli='gem list'

| gentags='ripper-tags -R --exclude=.git'

| geo='gem open'
| geoe='gem open -e'
| get_path='echo $PATH \| tr -s ":" "\n"'
| geun='gem uninstall'
| gf='git fetch'

| gfa='git fetch --all --prune --jobs=10'

| gfg='git ls-files \| grep'
| gfo='git fetch origin'
| gg='git gui citool'
| gga='git gui citool --amend'
| ggpull='git pull origin "$(git_current_branch)"'
| ggpur=ggu
| ggpush='git push origin "$(git_current_branch)"'

| ggsup='git branch --set-upstream-to=origin/$(git_current_branch)'

| ghh='git help'
| gignore='git update-index --assume-unchanged'
| gignored='git ls-files -v \| grep "^[[:lower:]]"'

| git-svn-dcommit-push='git svn dcommit && git push github $(git_main_branch):svntrunk'

| gk='\gitk --all --branches &!'

| gke='\gitk --all $(git log --walk-reflogs --pretty=%h) &!'

| gl='git pull'
| glg='git log --stat'
| glgg='git log --graph'
| glgga='git log --graph --decorate --all'

| glgm='git log --graph --max-count=10'

| glgp='git log --stat --patch'
| glo='git log --oneline --decorate'
| globurl='noglob urlglobber '

| glod='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ad) %C(bold blue)<%an>%Creset'\'
| glods='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ad) %C(bold blue)<%an>%Creset'\'' --date=short'

| glog='git log --oneline --decorate --graph'
| gloga='git log --oneline --decorate --graph --all'

| glol='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset'\'
| glola='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset'\'' --all'
| glols='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset'\'' --stat'

| glp=_git_log_prettily
| gluc='git pull upstream $(git_current_branch)'
| glum='git pull upstream $(git_main_branch)'
| gm='git merge'
| gma='git merge --abort'
| gmom='git merge origin/$(git_main_branch)'
| gmtl='git mergetool --no-prompt'

| gmtlvim='git mergetool --no-prompt --tool=vimdiff'

| gmum='git merge upstream/$(git_main_branch)'
| gp='git push'
| gpd='git push --dry-run'
| gpf='git push --force-with-lease --force-if-includes'
| 'gpf!'='git push --force'
| gpoat='git push origin --all && git push origin --tags'
| gpod='git push origin --delete'
| gpr='git pull --rebase'
| gpristine='git reset --hard && git clean --force -dfx'
| gpsup='git push --set-upstream origin $(git_current_branch)'
| gpsupf='git push --set-upstream origin $(git_current_branch) --force-with-lease --force-if-includes'
| gpu='git push upstream'
| gpv='git push --verbose'
| gr='git remote'
| gra='git remote add'
| grb='git rebase'
| grba='git rebase --abort'
| grbc='git rebase --continue'
| grbd='git rebase $(git_develop_branch)'
| grbi='git rebase --interactive'
| grbm='git rebase $(git_main_branch)'
| grbo='git rebase --onto'
| grbom='git rebase origin/$(git_main_branch)'
| grbs='git rebase --skip'

| grep='grep -i --color=auto'

| grev='git revert'
| grh='git reset'
| grhh='git reset --hard'
| grm='git rm'
| grmc='git rm --cached'
| grmv='git remote rename'
| groh='git reset origin/$(git_current_branch) --hard'
| grrm='git remote remove'
| grs='git restore'
| grset='git remote set-url'
| grss='git restore --source'
| grst='git restore --staged'
| grt='cd "$(git rev-parse --show-toplevel  \|\| echo .)"'
| gru='git reset --'
| grup='git remote update'
| grv='git remote --verbose'
| gsb='git status --short --branch'
| gsd='git svn dcommit'
| gsh='git show'
| gsi='git submodule init'

| gsps='git show --pretty=short --show-signature'

| gsr='git svn rebase'
| gss='git status --short'
| gst='git status'
| gsta='git stash push'
| gstaa='git stash apply'
| gstall='git stash --all'
| gstc='git stash clear'
| gstd='git stash drop'
| gstl='git stash list'
| gstp='git stash pop'
| gsts='git stash show --text'
| gstu='gsta --include-untracked'
| gsu='git submodule update'
| gsw='git switch'
| gswc='git switch --create'
| gswd='git switch $(git_develop_branch)'
| gswm='git switch $(git_main_branch)'
| gtl='gtl(){ git tag --sort=-v:refname -n --list "${1}*" }; noglob gtl'
| gts='git tag --sign'
| gtv='git tag \| sort -V'
| gunignore='git update-index --no-assume-unchanged'
| gunwip='git log --max-count=1 \| grep -q -c "\--wip--" && git reset HEAD~1'
| gup='git pull --rebase'
| gupa='git pull --rebase --autostash'
| gupav='git pull --rebase --autostash --verbose'
| gupom='git pull --rebase origin $(git_main_branch)'
| gupomi='git pull --rebase=interactive origin $(git_main_branch)'
| gupv='git pull --rebase --verbose'
| gwch='git whatchanged -p --abbrev-commit --pretty=medium'
| gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify --no-gpg-sign --message "--wip-- [skip ci]"'
| gwt='git worktree'
| gwta='git worktree add'
| gwtls='git worktree list'
| gwtmv='git worktree move'
| gwtrm='git worktree remove'
| hist='history \| grep'
| history=omz_history
| iI=ipython
| ii=bpython
| info='info --vi-keys'
| ivm=nvim
| j='jobs -l'
| jl=julia
| js=js78
| l='lsd -lAh --group-dirs first'
| la='lsd -lah --group-dirs first'
| lg=lazygit
| ll='lsd -lh --group-dirs first'
| lnn='xrandr --output DVI-D-0 --brightness'
| loadshell='source ~/.zshrc'
| ls='lsd --group-dirs first'
| lsa='ls -lah'
| manj='man --locale=ja'
| md=/home/baka/.asdf/shims/md
| mdir='mkdir -pv'
| mix_refresh=_mix_refresh
| ml=multipass
| mpvs='mpv --no-osc --osd-on-seek=no --no-resume-playback --input-ipc-server=/home/baka/.mpv/socket --wid=$WINDOWID'
| mpvss='mpv --shuffle --no-osc --osd-on-seek=no --no-resume-playback --input-ipc-server=/home/baka/.mpv/socket --wid=$WINDOWID'
| mpvw='mpv --wid=$WINDOWID'
| nai='sudo nala install'
| nali='nala list --installed'
| nap='sudo nala purge'
| nar='sudo nala remove'
| nas='nala search'
| nash='nala show'
| nau='sudo nala update'
| naug='sudo nala upgrade'
| nauu='sudo nala update && sudo nala upgrade'
| ncdu='ncdu --color=dark'
| neofetch='neofetch --ascii ~/drafts/ussr --disable gtk2 gtk3 packages theme icons'
| note='jupyter notebook'
| pip='noglob pip'
| pipgi='pip freeze \| grep'
| pipi='pip install'
| pipir='pip install -r requirements.txt'
| piplo='pip list -o'
| pipreq='pip freeze > requirements.txt'
| pipu='pip install --upgrade'
| pipun='pip uninstall'
| please='sudo $(fc -ln -1)'
| py=python
| pym='python manage.py'
| q=exit
| qq=exit
| qrelated_wall_audio='xwinwrap -ov -g 1920x1080+1920+0 -- mpv --no-resume-playback --shuffle -wid WID  --no-osc --no-osd-bar --loop-file --player-operation-mode=cplayer --panscan=1.0 --no-input-default-bindings --input-ipc-server=/home/baka/.mpv/socket /home/baka/Music/current/'
| rb=ruby
| rd=rmdir
| rday='redshift -x -m randr && redshift -m randr -O 3500 -b 0.9'
| rdayq='redshift -x -m randr && redshift -m randr -O 3500 -b 0.9 && exit'
| resync_it='rsync --delete --verbose --recursive --update --progress /mnt/hdd/Documents/ /mnt/backup/Documents/'
| rfind='find . -name "*.rb" \| xargs grep -n'
| rg='rg -S'
| right_wall='xwinwrap -ov -g 1920x1080+1920+0 -- mpv -wid WID  --no-osc --no-osd-bar --loop-file --player-operation-mode=cplayer --no-audio --panscan=1.0 --no-input-default-bindings'
| right_wall_audio='xwinwrap -ov -g 1920x1080+1920+0 -- mpv -wid WID  --no-osc --no-osd-bar --loop-file --player-operation-mode=cplayer --panscan=1.0 --no-input-default-bindings'
| rm=remove
| rnight='redshift -x -m randr && redshift -m randr -O 2600 -b 0.8'
| rnightq='redshift -x -m randr && redshift -m randr -O 2600 -b 0.8 && exit'
| rnn='xrandr --output HDMI-A-0 --brightness'
| roff='redshift -x -m randr'
| roffq='redshift -x -m randr && exit'
| rp='rspec --color'
| rpfd='rspec --color --format d'
| rr=ranger
| rrun='ruby -e'
| rserver='ruby -e httpd . -p 8080'
| screenkey_left='screenkey -p fixed -g 100%x10%+0%+90% -f "DejaVu Sans Mono Bold"'
| screenkey_right='screenkey -p fixed -g 100%x10%+100%+90% -f "DejaVu Sans Mono Bold"'
| server='ruby -run -e httpd . -p 8080'
| set_path='export PATH="${PWD}:${PATH}"'
| sgem='sudo gem'
| t='trans :ru'
| tI='trans :ru'
| tib='tig blame -C'
| til='tig log'
| tis='tig status'
| to=cd
| tran='trans -d -t ru -I'
| tranej='trans -I :ja en:'
| traner='trans -I :ru en:'
| tranje='trans -I :en ja:'
| tranre='trans -I :en ru:'
| tt=fg
| vac='source ./.venv/bin/activate'
| vad=deactivate
| venv='python3 -m venv .venv'
| vi=/usr/bin/vim
| vim=nvim
| vmi=nvim
| vv=vimv
| which-command=whence
| xcopy='xclip -i'
| xpaste='xclip -o'
| yl='yt-dlp -f mp4'
| yl-fast='yt-dlp -f best --external-downloader aria2c --external-downloader-args "-j 16 -s 16 -x 16 -k 1M" '
| ylnp='yt-dlp -f mp4 --no-playlist'
| ylpc='yt-dlp -f mp4 --yes-playlist -o "./%(channel)s/%(playlist)s/%(playlist_index)s-%(title)s-%(id)s.%(ext)s"'
| ylph='yt-dlp -f mp4 --yes-playlist -o "$HOME/Videos/%(channel)s/%(playlist)s/%(playlist_index)s-%(title)s-%(id)s.%(ext)s"'
