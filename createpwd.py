# create pwd, test with pytest
import os
import string
import random

def rdpwd():
    chars_low = string.ascii_lowercase 
    chars_dig = string.digits
    chars_up = string.ascii_uppercase
    chars_mark = string.punctuation

    size = random.randint(1, 3)
    my_list = []
    while True:
        for i in range(size):
            my_list.append(random.choice(chars_low))
        for i in range(size):
            my_list.append(random.choice(chars_dig))
        for i in range(size):
            my_list.append(random.choice(chars_up))
        for i in range(size):
            my_list.append(random.choice(chars_mark))
        if len(my_list) >=11:
            break
    # for i in my_list:
    #     print(i)
    if len(''.join(x for x in my_list)) == 12:
        return ''.join(x for x in my_list)
    else:
        return ''.join(x for x in my_list)[-13:-1]


# print(rdpwd())

def test_password():
    assert len(rdpwd()) == 12

if __name__ == '__main__':
    x = 0
    while True:
        os.system('pytest pwd01.py')
        x += 1
        if x >=100:
            break
