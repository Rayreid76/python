"""Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language. There are two steps to this process, building a dictionary and then gathering all the data from it. Write a function that can take in and print out any dictionary keys and values."""

def dict_print(dict):
    for key,val in dict.items():
        print("My",key,"is",val)
        
        

personal = {
    "name":"Raymond",
    "age":"42",
    "country of birth":"USA",
    "favorite language":"Italian"
}

dict_print(personal)