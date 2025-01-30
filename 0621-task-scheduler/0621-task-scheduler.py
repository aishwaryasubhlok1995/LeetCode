class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0 
        hm = {}
        heapList = []
        for i in range(len(tasks)):
            if tasks[i] not in hm:
                hm[tasks[i]] = 1
            else:
                hm[tasks[i]] += 1
        queueList = deque()
        for key in hm:
            heapq.heappush(heapList, -1 * hm[key])
        print(heapList)
        while queueList or heapList:
            time += 1
            if len(heapList) > 0:
                value = heapq.heappop(heapList)
                if value+1 < 0:
                    queueList.append([value+1, time + n])
            if len(queueList) > 0 and queueList[0][1] == time:
                heapq.heappush(heapList, queueList.popleft()[0])
        return time 

        