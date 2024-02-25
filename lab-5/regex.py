import re
from _ast import pattern


# 1
def match_ab(text):
    pattern = "ab*"
    if re.match(pattern, text):
        return "Found a match"
    else:
        return "No match."


print(match_ab("ab"))


# 2

def match_a23b(text):
    pattern = "ab{2,3}"
    if re.match(pattern, text):
        return "Found a match"
    else:
        return "No match."


print(match_a23b("abb"))


# 3
def lowercase_underline_sequence(text):
    pattern = r'[a-z]{1}(?:_[a-z]{1})+'
    return re.findall(pattern, text)


input_string = "some_words_are_j_ooined_by_underscores and others are not"
print(lowercase_underline_sequence(input_string))


# 4
def upper_after_lower(text):
    pattern = r'(?:[A-Z]{1}[a-z])+'
    return re.findall(pattern, text)


print(upper_after_lower("AoBfLookingforurboyfriendGive"))


# 5
def string_a_with_b_ending(text):
    pattern = r'[a-z]*a[a-z]*b$'
    if (re.match(pattern, text)):
        return "Match"
    else:
        return "No match."


print(string_a_with_b_ending("1zhusab"))


# 6
def replace_by_colon(text):
    pattern = r'[., ]'
    return re.sub(pattern, '|', text)


print(replace_by_colon("zhus.sas,lol "))


# 7
def replace_snakecase_on_camelcase(text):
    pattern = r'_([a-z])'
    return re.sub(pattern, lambda x: x.group(1).upper(), text)


print(replace_snakecase_on_camelcase('hello_world'))


# 8

def split_to_uppercase(text):
    pattern = r'[a-z]'
    return re.sub(pattern, lambda x: x.group().upper(), text)


print(split_to_uppercase("zhus"))


# 9
def insert_spaces(text):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1 \2', text)


print(insert_spaces('helloWorld'))


# 10
def camel_to_snake(text):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, lambda x: x.group(1) + '_' + x.group(2).lower(), text)

print(camel_to_snake('helloWorld'))