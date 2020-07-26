import pandas

df = pandas.read_csv("newFile.txt")
df = df.set_index("Id")
print(df)
print("Enter Contacts")


def add_in_file():
    ID = input('ID:-')
    Name = input("Name:-")
    Mobile = input("Mobile:- ")

    if ID != None and Name != None and Mobile != None:
        file = open("newFile.txt", 'a')
        file.write("\n" + ID + "," + Name + "," + Mobile)
        file.close()
        df1 = pandas.read_csv("newFile.txt")
        print(df1)
    else:
        print("Please enter the value.")


def add_in_dataFrame():
    ID = input('ID:-')
    Name = input("Name:-")
    Mobile = input("Mobile:- ")

    df_t = df.T

    df_t[ID] = [Name, Mobile]
    final = df_t.T
    print(final)
    final.to_csv("newFile.txt")


add_in_dataFrame()

