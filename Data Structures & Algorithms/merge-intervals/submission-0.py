class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []

        s, e = intervals[0][0], intervals[0][1]

        for interval in intervals[1:]:
            curr_s, curr_e = interval[0], interval[1]

            if curr_s <= e:
                e = max(e, curr_e)
            else:
                merged.append([s, e])
                s = curr_s
                e = curr_e

        merged.append([s, e])
        return merged