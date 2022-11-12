def split_and_join(line):
    # write your code here
    new_str=''
    for i in line:
        if i.isspace()==True:
            new_str+='-'
        else:
            new_str+=i

    return new_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)