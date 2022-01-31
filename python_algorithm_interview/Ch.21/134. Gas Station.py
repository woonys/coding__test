class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        station = 0
        while True:
            n_cnt = n
            idx = station
            gas_amount = gas[idx]
            for _ in range(n):
                n_cnt -= 1
                gas_amount -=cost[idx % n]
                #print("gas_amount-cost", gas_amount, cost[idx%n])
                gas_amount += gas[(idx+1) % n]
                #print("gas_amount+gas", gas_amount, gas[(idx+1)%n])
                if gas_amount <= 0:
                    station +=1
                    break
                idx += 1
            if n_cnt == 0:
                break
                
        if gas_amount >=gas[station]:
            return station
        else:
            return -1
        
        
        