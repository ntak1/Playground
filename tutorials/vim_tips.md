# Just some random vim tips

## Show line numbers
```vim
set number
```

## Markdown
To use the native markdown suport
```vim
set syntax=markdown
```
To recognise the .md files as markdown insert this on .vimrc
```vim
au BufNewFile, BufFilePre, BufRead *.md set filetype=markdown
```




