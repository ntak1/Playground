# Just some usefull commands on terminals

## Compress and Uncompress Files
### zip
```vim
zip -r filename.zip file1, file2, file3 ...
```
**Obs:** the -r is 'recursive, useful when working with directories.
 ### unzip
```vim
unzip filename
```
### tar
* To compress  
    ```vim
     tar -czvf name_of_file.tar.gz path/to/directory_or_file
    ```
    * c: create
    * z: compress
    * v: verbose
    * f: allows to specify the filename

* To uncompress
    ```vim
    tar -xzvf file_name.tar.gz
    ``` 
    * x: eXtract
