if __name__ == "__main__":
    pass

def encode(userinput):
    result = ""
    password = userinput
    for digit in range(len(password)):
        var1 = int(password[digit]) + 3
        result += str(var1)

def main():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")
    user = print("Please enter an option: ")
    if user == "1":
        userinput = print("Please enter your password to encode: ")
        encode(userinput)
        print("Your password has been encoded and stored!")
    if user == "2":
        pass






