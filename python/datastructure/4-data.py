#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
for i,k in a_dictionary.items():
    print(i,k,"\n")
print("--")
print(new_dict)
