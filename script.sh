#!/bin/zsh
mkdir ./temp/
cd temp/
echo "hello world!" > hello.txt
ls -ltra ../temp
ps axu
kill -HUP 666
echo $PATH > path.txt
find .. -name "hello.txt"  
find .. -name "*.png"
whereis echo
man ps | grep "Select all processes"
last > commands.txt
