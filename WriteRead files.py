# file = open("C:\\Users\\cympl.lp011\\Desktop\\Test Files\\NEW_File.txt","w")
# file.writelines("This is test data file")
# file = open("C:\\Users\\cympl.lp011\\Desktop\\Test Files\\NEW_File.txt","a") #Syntax to append new things to previous file without rewrite
# file.writelines("\n" + "And appended new line")
#
# file.close()
#
# file2 = open("C:\\Users\\cympl.lp011\\Desktop\\Test Files\\NEW_File1.txt","w")
# d = {"a": 1, "b": 2, "c": 3} #Dictionary
# for item, i in d.items(): #Loop to print dict key and values
#     file2.write(str(item) + ": ")
#     file2.write(str(i)+ "\n")
# file2.close()

# Read content of file
# file2 = open("oops.py","r") #"r+" used for read and write both
# print(file2.read())
# file2.close()

#with and as operations do not need close method

# with open("Testfile.tx","w") as fileNew:
#     fileNew.writelines(["1st line" + "\n", "2nd line" + "\n", "3rd line"])
# with open("Testfile.tx", "a") as fileNew:
#     fileNew.write("\nAppending new line for practice")
# with open("Testfile.tx","r") as readfile:
#     print(readfile.read())

















