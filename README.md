# Line Replacer
PURPOSE
this script will fix csv files that have carriage returns in file where there
should not be any.

EXAMPLE of the problem on the 4th line below.

number, name, category
3,	Bobby,	MW-W&E.......
3,	Bobby,	MW-W&E.......
3,	Bobby,	MW-W&E
.......
3,	Bobby,	MW-W&E.......
3,	Bobby,	MW-W&E.......

INSTRUCTIONS
1) make sure csv file and python script are in the same folder
2) Run the python script
3) Follow the instructions in the interactive script
4) The file is fixed

NOTES
It was made so that you can run it on computers within strict  security
environments. For this reason there are no libraries that need to be installed
and none were used in the script. It uses the second line in the csv to
determine the first character of each line. When this condition is not met it
knows that there is a carriage return in the line. It then bonds the line with
the previous line.
