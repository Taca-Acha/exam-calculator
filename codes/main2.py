corrects = ['152431243241523',
            '154321412351245']
points = ['222223333344444',
          '222233333344444']
checkN = int(input("채점할 과목을 선택해주세요.(0:수학 / 1:영어)[2023.09.29]"))

correctNum = corrects[checkN]

point = points[checkN]

while True:
    studentNum = input("input Your Answer:")
    p=','.join(point)
    c=','.join(correctNum)
    s=','.join(studentNum)
    pp=p.split(sep=',')
    cc=c.split(sep=',')
    ss=s.split(sep=',')
    isCorrect = ''
    isCorrectNum = 0
    z = 0

    if len(cc) != len(ss):
        print("please try again.")
        break

    def toInt(a):
        for i in range(len(a)):
            a[i] = int(a[i])

    toInt(cc)
    toInt(ss)
    toInt(pp)

    for i in range(len(cc)):
        if cc[i] != ss[i]:
            isCorrect = isCorrect + "X"
        elif cc[i] == ss[i]:
            isCorrectNum = isCorrectNum + pp[i]
            isCorrect = isCorrect + "O"

    for j in range(len(pp)):
        z = z + pp[j]

    print(f"답안:{correctNum}\n입력:{studentNum}\n결과:{isCorrect}\n점수:{isCorrectNum}/{z} 점")
