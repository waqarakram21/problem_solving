from statistics import mean
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        if i==query_name:
            average=mean(student_marks[i])
            result = format(average, '.2f')
            print(result)