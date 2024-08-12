class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # count = Counter(s)

        # window = set()
        # curSum = 0
        # lastPtr = -1
        # res = []

        # for i in range(len(s)):
        #     if s[i] not in window:
        #         curSum += count[s[i]]
        #         window.add(s[i])

        #     curSum -= 1

        #     if curSum == 0:
        #         res.append(i - lastPtr)
        #         lastPtr = i

        # return res

        # intervals = []
        # interval_map ={}
        # ans = []

        # for i in range(len(s)):
        #     if s[i] not in interval_map:
        #         interval_map[s[i]] = [i,i]
        #     else:
        #         interval_map[s[i]][1] = i
        
        # for interval in interval_map.values():
        #     intervals.append(interval)
        
        # intervals.sort(key=lambda x:x[0])
        # ans.append(intervals[0])

        
        # for i in range(1,len(intervals)):
        #     lastEnd = ans[-1][1]

        #     if intervals[i][0] <= lastEnd:
        #         ans[-1][1] = max(intervals[i][1],lastEnd)

        #     else:
        #         ans.append(intervals[i])


                
        # res = []
        # for start,end in ans:
        #     res.append(end - start + 1)

        # return res


        interval_map = {}
        ans = []

        for i in range(len(s)):
            if s[i] not in interval_map:
                interval_map[s[i]] = [i,i]
            else:
                interval_map[s[i]][1] = i
        end = 0
        start = -1
        for i in range(len(s)):
            end = max(interval_map[s[i]][1], end)

            if i == end:
                ans.append(end - start)
                start = i
        
        return ans