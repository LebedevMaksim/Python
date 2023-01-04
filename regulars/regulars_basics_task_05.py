# Task 4
# https://habr.com/ru/post/349860/#Zadachi__1


import re


text = """1.2 
  1. 
    1.0e-55  
      e-12   
  6.5E 
        1e-12  
  +4.1234567890E-99999           
  7.6e+12.5 
   99 """


def main(text_):

    for match in re.finditer(r'[^\s]+', text_, flags=re.MULTILINE):
        print(match[0],
              ' '*(20 - len(match[0])),
              'is legal' if re.fullmatch(r'(?:\+|-)?\d+(?:\.\d+)?(?:(?:e|E)(?:\+|-)\d+)?',
                                         match[0]) else 'is illegal')


if __name__ == '__main__':
    main(text)
