def get_length(elements:str):
    length:int = 0
    for i in elements:
        length+=1
    return length
print(get_length([91,1,2]))
print(get_length("hello"))