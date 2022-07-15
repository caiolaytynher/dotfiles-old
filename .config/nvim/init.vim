autocmd!

scriptencoding utf-8

if !1 | finish | endif

set exrc
set encoding=utf-8
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set ai
set si
set relativenumber
set nu
set nohlsearch
set hidden
set noerrorbells
set nowrap
set ignorecase
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set scrolloff=10
" set signcolumn=yes

set cursorline
highlight Visual cterm=NONE ctermbg=236 ctermfg=NONE guibg=Grey40
highlight LineNr cterm=none ctermfg=240 guifg=#2b506e guibg=#000000

augroup BgHighlight
    autocmd!
    autocmd WinEnter * set cul
    autocmd WinLeave * set nocul
augroup END

if &term =~ "screen"
    autocmd BufEnter * if bufname("") !~ "^?[A-Za-z0-9?]*://" | silent! exe '!echo -n "\ek[`hostname`:`basename $PWD`/`basename %`]\e\\"' | endif
    autocmd VimLeave * silent!  exe '!echo -n "\ek[`hostname`:`basename $PWD`]\e\\"'
endif

runtime ./plug.vim
if has("unix")
  let s:uname = system("uname -s")
endif

runtime ./maps.vim

au BufNewFile,BufRead *.fish set filetype=fish

autocmd FileType javascript setlocal shiftwidth=2 tabstop=2
autocmd FileType json setlocal shiftwidth=2 tabstop=2
autocmd FileType css setlocal shiftwidth=2 tabstop=2
autocmd FileType latex setlocal shiftwidth=2 tabstop=2 tw=67
autocmd FileType markdown setlocal shiftwidth=2 tabstop=2 tw=67

fun! TrimWhitespace()
    let l:save = winsaveview()
    keeppatterns %s/\s\+$//e
    call winrestview(l:save)
endfun

autocmd BufWritePre * :call TrimWhitespace()

if exists("&termguicolors") && exists("&winblend")
    syntax enable
    set termguicolors
    set winblend=0
    set wildoptions=pum
    set pumblend=5
    set background=dark
    colorscheme gruvbox
    highlight Normal guibg=none
    highlight NonText guibg=none
endif

