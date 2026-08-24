'''Write a function (you can name it whatever you want) that 
takes any word as a parameter, and returns all of its unique 
letters (without repetition) in alphabetical order.
For example, if when calling this function we pass the word 
"entertaining", it should return ['a', 'e', 'g', 'i', 'n', 'r', 't']'''
# def take_word(word):

def make_it(word):
    my_set = {x.lower() for x in word}  # transforma cada letra em minúscula
    my_list = sorted(list(my_set))      # ordena em ordem alfabética
    return my_list

print(make_it("Jooaaquuuiaim"))
