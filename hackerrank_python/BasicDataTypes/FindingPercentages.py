if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key, val in student_marks.items():
        avg = '{:.2f}'.format(sum(val)/len(val))
        val.append(avg)
        if key == query_name:
            print(val.pop())  
