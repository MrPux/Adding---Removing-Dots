#Function 'add_dots' takes a string and adds "." in between each letter.
    #E.g, calling add_dots("test") should return the string "t.e.s.t".

#Function 'remove_dots' removes all dots from a string. 
    #E.g, calling remove_dots("t.e.s.t") should return "test".

#By Calling both Functions remove_dots(add_dots(string))
#should return back te original string for any string.
 
def add_dots(string): 
    # Almost --> # s = ''.join([string[i] + '.' if string[i+1] != string[-1] else string[i] + '.' + string[i+1] for i in range(len(string) -1)])  
    # ''.join([string[i] + '.' if string[i+1] != None else string[i] + string[i+1] for i in range(len(string) -1)]) 
    # ''.join([(string[i] + '.'if string[i] != string[-1] else '' ) for i in range(len(string))])
    return  '.'.join(string)

def remove_dots(string):
    return string.replace('.', '')

    
a = add_dots("test") 
b = add_dots("Hello") 
c = add_dots("ComplexityFile") 
 
print(a) # t.e.s.t
print(b) # H.e.l.l.o
print(c) # C.o.m.p.l.e.x.i.t.y.F.i.l.e

print(remove_dots(a)) # test
print(remove_dots(b)) # Hello
print(remove_dots(c)) # ComplexityFile