import re
import collections


# with open('data.txt', "r") as file:

#     long_words = {'a': 1}     #{'word': *amount of unique sym* }
#     for line in file:
#         line = line.encode('utf-8').decode('unicode-escape')
#         words = re.findall(r'\b[A-Za-zäöüÄÖÜß]+\b', line)

#         for word in words:
#             uniq_amount = len(set(word))
#             min_uniq_dict = min(long_words.values())
#             if  len(long_words) <= 10:
#                 long_words[word]=uniq_amount
#             elif uniq_amount > min_uniq_dict:
#                 long_words = {key:val for key, val in long_words.items() if val != min_uniq_dict}
#                 long_words[word]=uniq_amount

# print("RESULT\n", long_words)



# with open('data.txt', "r") as file:
#     a = 0
#     long_words = {1:'a'}     #{*amount of unique sym*: 'word'}
#     for line in file:
#         line = line.encode('utf-8').decode('unicode-escape')
#         print(line)
#         a +=1
#         if a==15:
#             break


#говно
# def get_longest_diverse_words(file_path: str):
#     with open(file_path, encoding='utf-8', mode='r') as fi:
#         text = fi.read().encode('utf-8').decode('unicode-escape')
#         words = text.split(' ')
#         finale_list = sorted(words, key=lambda x: len(set(x)), reverse=True)  #
#         finale_list = finale_list[:10]  #

#     return finale_list

# print(get_longest_diverse_words('data.txt'))


#2
# with open('data.txt', "r") as file:

#     text = file.read().encode('utf-8').decode('unicode-escape')
#     counter_dict = collections.Counter(text)
#     for key in counter_dict:
#         print(f'{key} : {counter_dict[key]}')
#     rapest = min(counter_dict.values())
#     print(list(counter_dict.keys())[list(counter_dict.values()).index(rapest)])


#3
# with open('data.txt', "r") as file:

#     text = file.read().encode('utf-8').decode('unicode-escape')
#     punctuation_chars = re.findall(r'[^\w\s]', text)
#     punctuation_chars_dict = collections.Counter(punctuation_chars)
#     print(punctuation_chars_dict)


# #4
# with open('data.txt', "r") as file:

#     text = file.read().encode('utf-8').decode('unicode-escape')
#     non_ascii = re.findall(r'[^\x00-\x7F]', text)
#     non_ascii_dict = collections.Counter(non_ascii)
#     print(non_ascii_dict)
#     print(sum(non_ascii_dict.values()))




# with open('data.txt', "r") as file:

#     text = file.read().encode('utf-8').decode('unicode-escape')
#     non_ascii = re.findall(r'[^\x00-\x7F]', text)
#     non_ascii_dict = collections.Counter(non_ascii)
#     common = max(non_ascii_dict.values())
#     print(list(non_ascii_dict.keys())[list(non_ascii_dict.values()).index(common)])



#hw4

# global CACHE
CACHE = {}

def cache(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        CACHE[f'{len(CACHE)} call of initial one:'] = result
        return result
    return wrapper

@cache
def func(a, b):
    return (a**b)**2

# cache_func = cache(func)
# res = cache_func(2,3)
# print("result:\t", res)
# res = cache_func(3,2)
# print("result:\t", res)
print(func(2,3))
print(func(4,5))
print(CACHE)