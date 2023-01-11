my_string = "I love you"
my_string = list(my_string)
num1 = 3
num2 = 6

char1 = my_string[num1]
char2 = my_string[num2]

my_string[num2] = char1
my_string[num1] = char2
print("".join(my_string))


def solution(my_string, num1, num2):
    my_string = list(my_string)
    char1 = my_string[num1]
    char2 = my_string[num2]
    print(char1, char2)
    my_string[num2] = char1
    my_string[num1] = char2
    print(*my_string)
    return "".join(my_string)
