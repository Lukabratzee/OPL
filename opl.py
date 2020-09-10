import os.path
import re
import glob

# example - SLUS_200.74.Summoner

# path that points to PS2 game ISO's
path = glob.iglob('Y:\\Games\\PS2\\' + '**/**', recursive=True)

# compiling regex search. Looks for SLUS-, numbers and ()
slusRegex = re.compile(r'(SLUS-)(\d+)(.*)')
numberRegex = re.compile(r'(\d{3})(\d{2})')
pathRegex = re.compile(r'(?s:.*)(PS2\\)(.*)')

# 'good practice to declare' - Daddy Halloumi
path_folder = []

# converts returned result from tuple into str
def convert_tuple(tup):
    values = ''.join(map(str, tup))
    return values

# searches for filenames
for filename in path:

    match = slusRegex.findall(filename)
    path_folder.append(filename)
    tmp = path_folder[-1:]

    for x in match:
        # converts result to string
        values = convert_tuple(match)
        tmp = convert_tuple(tmp)
        # finds last instance of \\ to read parent dir
        tmp = pathRegex.findall(tmp)

        slus, numbers, bracketNumber = x
        numberMatch = numberRegex.findall(numbers)
        withDot = ".".join(list(numberMatch[0]))
        withDot = withDot + '.'

        # formatting vidya name
        up_dir = "".join(list(tmp[0]))
        up_dir = up_dir.replace('PS2\\', '')
        up_dir = up_dir.split('\\', 1)[0]

        # formatting ID (don't know how to do this cleaner)
        values = values.replace('-', '_')
        values = values.replace(numbers, withDot)
        values = values.replace(bracketNumber, '')
        values = values.replace(' ', '')
        values = values.replace('"', '')
        values = values.replace('\'', '')
        values = values.replace('(', '')
        values = values.replace(')', '')
        values = values.replace(',', '')

        preview = values + up_dir + '.iso'
        print (preview)
        os.rename(filename, 'Y:\\Games\\PS2\\' + preview)
