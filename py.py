def longest_slide_down(pyramid):
    buf = [[pyramid[0][0]]]
    for t in range(1,len(pyramid)):
        buf.append([])
    print(pyramid)
    print(buf)
    for t in range(1,len(pyramid)):
        for r in range(0,len(pyramid[t])):
            buf[t][r]
    return
longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])