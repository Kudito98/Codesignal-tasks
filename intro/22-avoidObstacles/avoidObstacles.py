def solution(inputArray):
    obs = sorted(inputArray)
    jump_dist = 1
    obstacle_hit = True
  
    while(obstacle_hit):          
        obstacle_hit = False
        jump_dist += 1
    
        for i in range(len(obs)):
            if obs[i] % jump_dist == 0:             
                obstacle_hit = True
                break
  
    return jump_dist
