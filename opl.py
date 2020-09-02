import os
import re
import glob

# example - SLUS_200.74.Summoner


# path that points to PS2 game ISO's
path = glob.iglob('Y:\\Games\\PS2\\' + '**/**', recursive=True)

# compiling regex search. Looks for SLUS-, numbers and ()
slusRegex = re.compile(r'(SLUS-)(\d+)(.*)')
numberRegex = re.compile(r'(\d{3})(\d{2})')
# converts returned result from tuple into str
def convert_tuple(tup): 
    values = ''.join(map(str, tup))
    return values

# searches for filenames
for filename in path:
    match = slusRegex.findall(filename)

    values = convert_tuple(match)

    for x in match:

        slus, numbers, bracketNumber = x

        values = values.replace('-', '_')
        numberMatch = numberRegex.findall( numbers )
        withDot = ".".join(list(numberMatch[0]))
        withDot = withDot + '.'
        afterDot = ".".join(list(bracketNumber[0:1]))

        values = values.replace(numbers, withDot)
        values = values.replace(bracketNumber, afterDot)
        print (values)
        values = values.replace(' ', '')
        values = values.replace(',', '')
        print (values)

        

