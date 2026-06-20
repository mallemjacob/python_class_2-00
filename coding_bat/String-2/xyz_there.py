
# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
    found = False
    if str[0:3] == 'xyz':
        found = True
    else:
        for i in range(1, len(str) - 2):
            if str[i-1] != '.' and str[i] == 'x' and str[i+1] == 'y' and str[i+2] == 'z':
                found = True
    return found


xyz_there('abcxyz')
xyz_there('abc.xyz')
xyz_there('xyz.abc')
