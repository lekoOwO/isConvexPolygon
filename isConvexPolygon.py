def line(point1, point2):  # point1, point2 = [x1, y1]
    if not point1[0] - point2[0] == 0:
        a = (point1[1] - point2[1]) / (point1[0] - point2[0])
        b = -1
        c = point1[1] - point1[0] * a
    else:
        a = 1
        b = 0
        c = -point1[0]
    return [a, b, c]  # ax+by+c=0

def isSameSign(nums): # if numbers in nums are same-signed
    def numOfNotZero(numbers): # return the first index of non-zero object in list
        for i in list(range(len(numbers))):
            if not numbers[i] == 0:
                return i 
        return 'All the Numbers are 0.'

    if not isinstance(numOfNotZero(nums), int):
        return 'All points are in a line.'
    else: 
        for i in nums:
            if i*nums[numOfNotZero(nums)] < 0:
                return False 
        return True

def isAtSameSide(points, line): # points = [point1, point2 ...]
    sub = lambda point, line:line[0]*point[0] + line[1]*point[1] + line[2] # return the value of ax+by+c
    return isSameSign(list(sub(i, line) for i in points))

def isConvexPolygon(points): # points = [point1, point2 ... ]
    points.append(points[0])
    for i in list(range(len(points)))[:-1]:
        if i == 0 and isinstance(isAtSameSide(points, line(points[i], points[i+1])), str): # only check for one time
            return "It's a line." 
        if not isAtSameSide(points, line(points[i], points[i+1])):
            return False
    return True

if __name__ == "__main__":
    print(isConvexPolygon([[float(k) for k in i[1:-1].split(',')] for i in input("請輸入欲檢測多邊形之所有點座標。\ne.g.: (1,0) (2,0) (1.5,1) (1.5,1.3e+1)\n\n").split(" ")]))

            
            

            





