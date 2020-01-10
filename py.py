def longest_slide_down(pyramid):
    buf = [
            [
                [
                    pyramid[0][0]
                ]
            ]
          ]
    for t in range(1,len(pyramid)):
        arr = []
        for r in range(0,len(pyramid[t])):
            arr.append([0])
        buf.append(arr)
    print(pyramid)
    print(buf)
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
                buf[t][r]=currentArr
            elif (r==len(pyramid[t])-1) and (t!=1):
                print('->',buf[t-1][r-1])
                currentArr = []
                for n in range(0,len(buf[t-1][r-1])):
                    print('!')
                    currentArr.append(buf[t-1][r-1][n]+pyramid[t][r])
                print(currentArr,'<-')
                buf[t][r-1] = currentArr
            #else: 
            #    currentArr = []
            #    for n in range(0,len(buf[t-1][r])):
            #        currentArr.append(buf[t-1][r][n]+pyramid[t][r])
            #    for n in range(0,len(buf[t-1][r-1])):
            #        currentArr.append(buf[t-1][r-1][n]+pyramid[t][r])
            #    buf[t][r] = currentArr
    print(buf[len(buf)-1])
                    
    return ''
longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])