if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if name == query_name:
        Sum=sum(scores)
        result_format= "{:.2f}".format(float(Sum/3))
        print (result_format)
        
