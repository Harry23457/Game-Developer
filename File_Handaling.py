#three modes of working with a file-read,write,append

#creating a new file
with open("short_story.txt","w") as file:
    file.write("hello,world!")

with open("short_story.txt") as file:
    print(file.read())

#adding
with open("short_story.txt","a") as file:
    file.write("python is great!")

#printing/reading the contents of a file
with open("short_story.txt","r") as file:
    print(file.readline())
    print(file.read())

#caution--OPENING AN EXISTING FILE IN "WRITE" MODE
with open("short_story.txt","w") as file:
    file.write("oh no!!!What did i do!!!")
       
with open("short_story.txt","r") as file:
    print(file.read())    
