"Configurações para o VIM.
"Fazer um clone do Vumdle na pasta .vim na home
"Sempre salvar e instalar tudo com PluginInstall"





" Disable compatibility with vi which can cause unexpected issues.
set nocompatible

" Enable type file detection. Vim will be able to try to detect the type of file in use.
filetype on

" Enable plugins and load plugin for the detected file type.
filetype plugin on

" Load an indent file for the detected file type.
filetype indent on
" Turn syntax highlighting on.
syntax on
" Add numbers to each line on the left-hand side.
set number
set nocompatible              " be iMproved, required
filetype off                  " required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

Plugin 'delimitMate.vim'
Plugin 'joshdick/onedark.vim'
Plugin 'itchyny/lightline.vim'
Plugin 'sonph/onehalf', { 'rtp': 'vim' }
Plugin 'dracula/vim', { 'name': 'dracula' }
set laststatus=2
colorscheme onehalfdark
