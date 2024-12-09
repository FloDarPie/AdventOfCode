def is_nice(s):
    vowels = 'aeiou'
    vowel_count = sum(s.count(v) for v in vowels)
    if vowel_count < 3:
        return False
    if not any(s[i] == s[i+1] for i in range(len(s)-1)):
        return False
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    return True

with open('day5input.txt') as f:
    strings = f.readlines()

nice_strings = [s for s in strings if is_nice(s.strip())]
print(len(nice_strings))


def is_nice(s):
    if not any(s[i:i+2] in s[i+2:] for i in range(len(s)-2)):
        return False
    if not any(s[i] == s[i+2] for i in range(len(s)-2)):
        return False
    return True

with open('day5input.txt') as f:
    strings = f.readlines()

nice_strings = [s for s in strings if is_nice(s.strip())]
print(len(nice_strings))
