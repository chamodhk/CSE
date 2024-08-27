KEYS = [['.'],
         ['a','b','c'],
         ['d','e','f'],
         ['g','h','i'],
        ['j','k','l'],
        ['m','n','o'],
         ['p','q','r','s'],
         ['t','u','v'],
         ['w','x','y','z'],
         [' ']]
         


NEXT_KEY = 0.4
KEY_PRESS = 0.2
SAME_KEY  = 0.7

def get_key_press_time(char, key):
    index = key.index(char)+1
    time = index*KEY_PRESS
    

    return time

text = input().lower()
time = 0
for char in text:
    for key in KEYS:
        if char in key:
            try:
                if previous_key == KEYS.index(key):
                    time += SAME_KEY
                else:
                    time += NEXT_KEY
                    previous_key = KEYS.index(key)
            except NameError:
                previous_key = KEYS.index(key)

            time += get_key_press_time(char, key)
            

print(format(time, '.2f'))

                    


