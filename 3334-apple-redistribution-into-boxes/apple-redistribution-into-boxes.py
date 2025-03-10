class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """

        total_apples = sum(apple)
        capacity.sort(reverse = True)

        num_boxes = 0

        for cap in capacity:
            total_apples -= cap
            num_boxes += 1
            if total_apples <= 0:
                return num_boxes

        return num_boxes
        