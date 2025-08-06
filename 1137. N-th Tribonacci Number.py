def minCostClimbingStairs(cost) -> int:
    idx = 0 if cost[0] < cost[1] else 1
    count = 0
    while idx < len(cost) - 1:
        count += cost[idx]  
        
        if cost[idx + 1] < cost[idx + 2]:
            idx += 1
        else:
            idx += 2

    return count


print(minCostClimbingStairs([10,15,20]))