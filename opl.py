import os
import re
import glob


# path that points to PS2 game ISO's
path = glob.iglob('Y:\\Games\\PS2\\' + '**/**', recursive=True)

# compiling regex search. Looks for SLUS-, numbers and ()
s_number = re.compile(r'(SLUS-)(\d+)(.*)')

# converts returned result from tuple into str
def convert_tuple(tup): 
    values = ','.join(map(str, tup))
    return values

# searches for filenames
for filename in path:
    match = s_number.findall(filename)
    values = convert_tuple(match)

    # if one matches, begin formatting
    if values:
        # - to _
        values = values.replace('-', '_')
        # 5 digits to 3 digits, period, then remainder
        # i.e 55555 to 555.55
        values = re.sub('(?<={5})', '(?<={3})(?>=\.)', values)
        print(values)
