"""
Part I

Create a function called draw_stars() that takes a list of numbers and prints out *.

Part II

Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
"""
x = [4, 6, 1, 3, 5, 7, 25]
#x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
star = ""
l = []
def draw_stars(arr):
    for i in range(0,len(arr)):
        if type(arr[i]) is int:
            print("*"*arr[i])
        elif type(arr[i]) is str:
            star = arr[i]
            star.split()
            l = star[0].rstrip(star.lower())
            print(l)
            
            
draw_stars(x)

print("")
print("")
print("Mixed list")
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)