def longest_slide_down(pyramid):
    buf = [
            [
                [
                    pyramid[0][0],
                ]
            ]
          ]
    for t in range(1,len(pyramid)):
        arr = []
        for r in range(0,len(pyramid[t])):
            arr.append([0])
        buf.append(arr)
    for t in range(1,len(pyramid)):
        for r in range(0, len(pyramid[t])):
            if (r==0):
                currentArr = []
                #print(buf[t-1][r])
                for n in range(0,len(buf[t-1][r])):
                    #print('jk')
                    #print(n,r,t,buf[t-1][r])
                    #print(pyramid[t][r],'<-')
                    currentArr.append(buf[t-1][r][n]+pyramid[t][r])
                #print(currentArr,'|')
                max = 0
                flag = False
                if (len(currentArr) > 2):
                    flag = True
                    for w in range(0,len(currentArr)):
                        if (max<currentArr[w]):
                            max = currentArr[w]
                if(flag):
                    buf[t][r]=[max]
                else:
                    buf[t][r]=currentArr
            elif (r==len(pyramid[t])-1):
                #print('->',buf[t-1][r-1])
                currentArr = []
                for n in range(0,len(buf[t-1][r-1])):
                    #print('!')
                    currentArr.append(buf[t-1][r-1][n]+pyramid[t][r])
                #print(currentArr,'<-')
                max = 0
                flag = False
                if (len(currentArr) > 2):
                    flag = True
                    for w in range(0,len(currentArr)):
                        if (max<currentArr[w]):
                            max = currentArr[w]
                if(flag):
                    buf[t][r]=[max]
                else:
                    buf[t][r]=currentArr
            else: 
                currentArr = []
                for n in range(0,len(buf[t-1][r])):
                    currentArr.append(buf[t-1][r][n]+pyramid[t][r])
                for n in range(0,len(buf[t-1][r-1])):
                    currentArr.append(buf[t-1][r-1][n]+pyramid[t][r])
                max = 0
                flag = False
                if (len(currentArr) > 2):
                    flag = True
                    for w in range(0,len(currentArr)):
                        if (max<currentArr[w]):
                            max = currentArr[w]
                if(flag):
                    buf[t][r]=[max]
                else:
                    buf[t][r]=currentArr
    #print(buf[len(buf)-1])123123
    lastArr = len(buf)-1
    maxNum = 0
    for t in range(0,len(buf[lastArr])):
        for r in range(0,len(buf[lastArr][t])):
            if (buf[lastArr][t][r]>maxNum):
                maxNum=buf[lastArr][t][r]
    print(maxNum)
    return maxNum
longest_slide_down([
    [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ]
)
