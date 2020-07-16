#interpolation search
def interpolation_search(lis , x):
    pos = (x-list[0])*(len(list)-1) // (list[-1]-list[0])
    if 0 < pos < (len(lis)):
        if x == list[pos]:
            print("element found")
            return True
        elif x > list[pos]:
            interpolation_search(list[pos:], x)
        else:
            interpolation_search(list[:pos], x)
    else:
        print("element not found")
        return False


list = [4, 5, 6, 7, 8, 9, 80, 90]
x = int(input("enter the number you want to search: "))
result = interpolation_search(list, x)