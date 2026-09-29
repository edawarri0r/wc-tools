# WC Tools

## This app made based of  [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc/)
This challenge is to build your own version of the Unix command line tool wc!

## Environment
<ol>
    <li><a href="https://www.python.org/downloads/">Python 3.14.7</a></li>
    <li><a href="https://code.visualstudio.com/">Visual Studio Code</li> 
</ol>

## Feature
<ol>
  <li>Count number of bytes in the file</li>
  <li>Count number of lines in the file</li>
  <li>Count number of words in the file</li>
  <li>Count number of characters in the file</li>
</ol>

## How to Run 
## Make sure Environment already fulfilled
 - Clone Project or Download Zip into local
 - Open Visual Studio and Open Folder to the project (If Download Zip then extract first)
 - Open Terminal in Visual Studio(ctrl + shift + `), make sure that directory is set into the folder
 - You can run the project by typing `python wc-tools.py [options] [filename.txt]` at the terminal

   Example:
   System will be returning number of bytes using `python wc-tools.py -c test.txt`
   
   System will be returning `bytes`,`lines`,`words` respectively if no options added using `python wc-tools.py test.txt`


  [options]
  word count: `-w`
  line count: `-l` 
  character count: `-m`
  byte count: `-c` 



