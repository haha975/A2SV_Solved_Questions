def split_and_join(line):
    # write your code here
    li=line.split(" ")
    answer="-".join(li)
    return answer

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
