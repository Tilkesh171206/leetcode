class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        a_a=sum(days[:int(arriveAlice[0:2])-1])+int(arriveAlice[3:5])
        l_a=sum(days[:int(leaveAlice[0:2])-1])+int(leaveAlice[3:5])
        a_b=sum(days[:int(arriveBob[0:2])-1])+int(arriveBob[3:5])
        l_b=sum(days[:int(leaveBob[0:2])-1])+int(leaveBob[3:5])


        return max(0,min(l_a,l_b)-max(a_a,a_b)+1)
