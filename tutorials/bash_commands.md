# Just some usefull commands on terminals

## Compress and Uncompress Files
### zip
```bash
zip -r filename.zip file1, file2, file3 ...
```
**Obs:** the -r is 'recursive, useful when working with directories.
 ### unzip
```bash
unzip filename
```
### tar
* To compress  
    ```bash
     tar -czvf name_of_file.tar.gz path/to/directory_or_file
    ```
    * c: create
    * z: compress
    * v: verbose
    * f: allows to specify the filename

* To uncompress
    ```bash
    tar -xzvf file_name.tar.gz
    ``` 
    * x: eXtract
### shh and scp
syntax:
```bash
    scp <file> <destination>
```
Examples:
```
    scp megaupload tux@192.168.254.156:/home/tux/Public
```
scp arquivo.txt lsantos@192.168.254.92:
