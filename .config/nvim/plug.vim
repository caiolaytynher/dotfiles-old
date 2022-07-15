if has("nvim")
  let g:plug_home = stdpath('data') . '/plugged'
endif

call plug#begin()

Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-rhubarb'

if has("nvim")
  Plug 'hoob3rt/lualine.nvim'
  Plug 'nvim-telescope/telescope.nvim'
  Plug 'morhetz/gruvbox'
  Plug 'dracula/vim',  { 'as': 'dracula' }
endif

call plug#end()
