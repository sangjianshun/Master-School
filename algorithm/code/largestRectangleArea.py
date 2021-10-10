class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)==0:
            return 0
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            if len(stack) == 1 or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) >1 and heights[i] < heights[stack[-1]]:
                    index = stack.pop()
                    tmp = heights[index] * (i - stack[-1] - 1)
                    max_area = max(max_area, tmp)
                stack.append(i)
            # print(stack)
        while len(stack)>1:
            index = stack.pop()
            tmp = heights[index] * (len(heights) - stack[-1] -1)
            max_area = max(max_area, tmp)
        return max_area

print(Solution().largestRectangleArea([3,1,3,2,2]))