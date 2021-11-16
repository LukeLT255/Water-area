def waterArea(heights):
    if len(heights) == 0:
        return 0

    leftIdx = 0
    rightIdx = len(heights) - 1
    surfaceArea = 0
    leftMax = heights[leftIdx]
    rightMax = heights[rightIdx]

    while leftIdx < rightIdx:
        if heights[leftIdx] < heights[rightIdx]:
            leftIdx += 1
            leftMax = max(leftMax, heights[leftIdx])
            surfaceArea += leftMax - heights[leftIdx]
        else:
            rightIdx -= 1
            rightMax = max(rightMax, heights[rightIdx])
            surfaceArea += rightMax - heights[rightIdx]

    return surfaceArea

if __name__ == '__main__':
    length = input('Please enter a number 0 or greater that will represent the length of pillars' + '\n')
    print('Pillar heights can be from size 0, meaning no pillar, to anything greater than 0')
    pillarHeights = [int(input('Pillar height ' + str(i+1) + ': ')) for i in range(int(length))]
    print(waterArea(pillarHeights))

