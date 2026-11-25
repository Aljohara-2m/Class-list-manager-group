# Class List Manager - Group 9
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====

# Written by: Aljohara (task 2)
def search_name(names, name):
    for n in names:
        if n == name:
            return True
    return False


# Written by: Eithar (task 1)
def count_names(names):
    return len(names)



# Written by: Khayal (Task 6)
def to_upper(names):
    upper_names = []
    for name in names:
        upper_names.append(name.upper())
    return upper_names



def main():

    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Is Sara in the list?", search_name(names, "Sara"))
    print("Number of names:", count_names(names))
    print("Uppercase names:", to_upper(names)) #Khayal
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))


main()
