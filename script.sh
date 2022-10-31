#!/bin/zsh
# make directory in the current location (preferably your user home directory)
mkdir temp/
# change directory to the newly created folder temp
cd temp/
# write hello world to the standard output of your shell session and forward the output into the file hello.txt
echo "hello world!" > hello.txt
# list directory contents with the parameters l (List files in the long format), t (Sort by descending time modified), r (Reverse the order of the sort) and a (Include directory entries whose names begin with a dot - so it shows also hidden files and directories).
ls -ltra ../temp
# process status with parameters a (Display information about other users' processes as well as your own), x (include processes which do not have a controlling terminal)
ps ax
# kill (very gently by sending the hangup signal (SIGHUP) to the process with PID 666
kill -HUP 666
# write the contents of the shell environment variable $PATH (available in every shell session)
echo $PATH > path.txt
# find files with the name hello.txt starting one directory from the current directory, since you changed to the temp folder earlier it's starts fromt the directory where the script.sh file is located
find .. -name "hello.txt"
# same search only different param
find .. -name "*.png"
# where is the binary of the program echo located
whereis echo
# display the man page of process status (ps) send the output to another program called grep (file pattern searcher). this way the output is filtered to display only lines that contain "Select all processes"
man ps | grep "Select all processes"
# execute history and limit the output to 10
history | tail -10  > commands.txt
