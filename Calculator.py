def Add(numbers):
    numbers = numbers.replace("\n" , ",")
    list = numbers.split(",")
    if len(list) == 1 and list[0] == "":
        return 0

    totalvalue = 0;
    for element in list:
        print(element)
        totalvalue += int(element)

    return (totalvalue)


