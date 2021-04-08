def str_rev(s):
    str_list = list(s.split(" "))
    str_list.reverse()
    reverse_str = " "
    reverse_str = reverse_str.join(str_list)
    print(f"String in reversed order : {reverse_str}")
    exit()


def validate():
    while True:
        inp_str = input("Enter String To Be Reversed : ")
        if len(inp_str) == 0 or any(char.isdigit() for char in inp_str):
            print("Please Enter Valid String.")
        else:
            str_rev(inp_str)


if __name__ == '__main__':
    validate()

