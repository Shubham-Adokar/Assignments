def find_long_word(str_list, num):
    print(f"New List containing list elements having length more than {num} : ",
          [word for word in str_list if len(word) > num])
    exit()


def take_input():
    while True:
        inp = input("Enter list elements separated by space : ")
        input_list = []
        if len(inp) == 0:
            print("Empty list not allowed")
        else:
            input_list = inp.split(" ")
            while True:
                try:
                    num = int(input("Enter Length : "))
                    find_long_word(input_list, num)
                except ValueError:
                    print("Enter Valid Integer Value")


if __name__ == '__main__':
    take_input()

