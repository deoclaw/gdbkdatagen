from faker import Faker
# This program prints out a number of fake names and fake numeric grades to create a fake gradebook

# This is an attempt at automating fake data for an assignment given to my students.

# Probably would have been less effort to just make things up by hand. YOLO


fake = Faker()

print("This program prints out a number of fake names and fake numeric grades to create a fake gradebook.")

testAmt = int(input("\nHow many fake tests do you want to include? "))

stuAmt = int(input("\nHow many fake students do you want to include? "))
delimeter = input("\nWhat delimeter would you like to use for each column? E.g. \\t for tab, , for comma ")
filename = input("\nThis will save as a text file with extension .txt. What do you want to call this file? ")


with open(filename+".txt", "w") as f:
    # iterate thru students with internal iteration of fake grades

    for student in range(stuAmt):
        f.write(fake.name()+delimeter)
        for test in range(1, testAmt+1): #did start at 1 and stop at amt+1 so i could control delimeter at end
            if test == testAmt:
                f.write(str(fake.pyint(50, 100)))
            else:
                f.write(str(fake.pyint(50, 100))+delimeter)
        f.write("\n")
