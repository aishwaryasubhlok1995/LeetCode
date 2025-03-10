class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        noOfBoats = 0 
        i = 0 
        j = len(people) - 1
        while i < j:
            noOfBoats += 1
            if people[i] + people[j] > limit:
                j -= 1
            elif people[i] + people[j] <= limit:
                i += 1
                j -= 1
        if i == j:
            return noOfBoats + 1
        return noOfBoats