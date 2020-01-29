#!/usr/bin/env python3

import random
import string

def password(length):
    pw = str()
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
      pw = pw + random.choice(characters)
    return(pw)

print(password(16))
