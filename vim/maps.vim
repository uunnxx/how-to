nmap <silent> <nowait><leader>u :UndotreeToggle<cr>
" nmap <silent> <nowait><leader>n :TagbarToggle<cr>
nmap <silent> <nowait><leader>n :Vista!!<cr>
" nmap <silent> <nowait><space>tt :Vista finder<cr>

" FUNCTION_KEYS:
nmap <silent> <F1> :vert help normal-index<cr>
imap <silent> <F1> <esc>:vert help insert-index<cr>

map <silent> <F2> :update $MYVIMRC <bar> source $MYVIMRC <cr>
map <silent> <F3> :tabnew $MYVIMRC <bar> tcd %:h<cr>


" Custom comma motion mapping
" nmap di, f,dT,
" nmap ci, f,cT,

" Delete || change an argument:
" nmap da, f,ld2F,i,<esc>l
" nmap ca, f,ld2F,i,<esc>a

" Delete || change surrounding characters
" noremap ds{ F{xf}x
" noremap cs{ F{xf}xi

" noremap ds" F"x,x
" noremap cs" F"x,xi

" noremap ds' F'x,x
" noremap cs' F'x,xi

" noremap ds( F(xf)x
" noremap cs( F(xf)xi

" noremap ds) F(xf)x
" noremap cs) F(xf)xi







" Select word under cursor and search 
vnoremap <silent> * :call VisualSelection('f', '')<cr>
vnoremap <silent> # :call VisualSelection('b', '')<cr>
vnoremap // y/\V<C-R>=escape(@",'/\')<cr><cr>








" Insert a space before current character
" nnoremap <silent> <space><space> i<TAB><esc>l

" Continuous visual shifting (do not exit Visual mode)
" `gv` means to reselect previous visual area, see https://goo.gl/m1UeiT
" xnoremap < <gv
" xnoremap > >gv




" Transfer text between two VIM instances
" Copy and paste & cut and paste between different Vim sessions
nnoremap <space>Y :!echo ""> ~/.vi_tmp<cr><cr>:w! ~/.vi_tmp<cr>
vnoremap <silent>map <space>Y :w! ~/.vi_tmp<cr>
nnoremap <space>X :!echo ""> ~/.vi_tmp<cr><cr>:w! ~/.vi_tmp<cr>
vnoremap <space>X :w! ~/.vi_tmp<cr>gvd
nnoremap <space>P :r ~/.vi_tmp<cr>
" vmap <leader>wr :w! expand("%:p:h")/



" Paste spaces without leaving command mode
nnoremap <silent><space>o :<C-u>call append(line("."),   repeat([""], v:count1))<cr>
nnoremap <silent><space>O :<C-u>call append(line(".")-1, repeat([""], v:count1))<cr>





" Man pages:
nnoremap <nowait><space>kv :Vman <C-R><C-W><cr>
nnoremap <nowait><space>kk :Man <C-R><C-W><cr>

nnoremap <silent> <PageUp> <C-U>
vnoremap <silent> <PageUp> <C-U>
inoremap <silent> <PageUp> <C-\><C-O><C-U>

nnoremap <silent> <PageDown> <C-D>
vnoremap <silent> <PageDown> <C-D>
inoremap <silent> <PageDown> <C-\><C-O><C-D>


" Zeal Vim
" default keymaps:
nmap <leader>z <Plug>Zeavim
vmap <leader>z <Plug>ZVVisSelection
" nmap gz <Plug>ZVOperator
nmap <leader><leader>z <Plug>ZVKeyDocset
