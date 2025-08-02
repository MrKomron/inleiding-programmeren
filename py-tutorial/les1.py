def romanToInt(s):
    romeinse_nums={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }

print(romanToInt("III"))
print(romanToInt("V"))
print(romanToInt("MCMXCIV"))  # Output: 1994

