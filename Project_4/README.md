# Three little projects

## Project 1 - parser_1.py

Here after compiling with some comma-seperated values data will be printed out on console. I made it so the day of the weeks can be from any day to any other, but max length is 7 (mon-sun, sun-sat, etc).

```
python3 parser_1.py styczeń,luty pn-wt,pt r,w
python3 parser_1.py styczeń,marzec pn-cz,śr-pn
```

After the first consol execution we should see:

```
Styczeń poniedziałek rano
Styczeń wtorek wieczorem
Luty piątek rano
```

# Project 2 - copy_all_lines.py

This was a weird one. Make a copy of a file, but make it line-by-line. Okay i guess. A copy is made in this very way. This is how it should be run.

```
python3 copy_file.py in.txt out.txt
```

# Project 3 - parser_3.py

I made it a little different. I make **only** the directories that would have been printed out in parser_1.py, but in english B). Everything is stored at DATA_3 direcotry.

After executing like this:

```
python3 parser_3.py --months january february march --days mon-tue fri fri-wed --time m e m e 
```

The directories will be created with csv files in them. 
The only thing that is gonna print is the total sum of the time of computation of model A's. As it is a random sample I'll not provide any examples lol.