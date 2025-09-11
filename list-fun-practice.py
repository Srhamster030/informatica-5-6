def main():
    length(values)
def values():
    value_list = []
    while True:
        value = int(input("Enter value: "))
        if (value != 0):
            value_list.append(value)
            print(value_list)
            value_list.sort()
            ordered_list = sorted(value_list)
            print(ordered_list)
            continue
        else:
                break
def length(list):
     return len(list)
