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
## To recognise the .md files as markdown insert this on .vimrc
```vim
au BufNewFile, BufFilePre, BufRead *.md set filetype=markdown
```
## Find and replace.
```vim
:%s/find/replace/gc
```
The gc means it will ask for confirmation before making any change.
We can also comment multiple line using the substitution, as follows:
```vim
:21,22s/^/###
```
## Undo
On command mode type:
```vim
u
```

