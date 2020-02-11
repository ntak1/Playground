"VISUALIZATION"
set number          "show line number on the left
set ruler           "Show the col number"

"TABS AND IDENTATION"
set ts=4	        "tab = 4 spaces
set expandtab       "all tabs will be replaced by spaces
set shiftwidth=4    "when using shift to ident?"
set softtabstop=4   
set autoindent

"FIX BUGGED BACKSPACE"
set backspace=indent,eol,start

set backup
set nocompatible

"SYNTAX"
au BufNewFile,BufFilePre,BufRead *.md set filetype=markdown
syntax on

"CLOSING"
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
