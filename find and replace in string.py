filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
for i in filenames:
    if(i.endswith(".hpp")):
        i=i.replace(".hpp",".h")
        newfilenames.append(i)
    else:
        newfilenames.append(i)


print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
