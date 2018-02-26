### Fun for CS 131
import itertools


def grid_maker(n): 

    servers = n*n   #number of servers
    infected = n - 1 #number of infected servers
    grid = [ 0 for a in range(servers)] #list representing grid, with all servers uninfected
    grid = grid[:-infected] + infected * [2] #infect last servests in grid

    all_infections = list(itertools.permutations(grid))  # !!PROBLEM!! create all permutations of infection (touple)
    all_infections = [list(a) for a in all_infections]   # Convert touple to lists
    

    all_infections.sort()
    all_infections = list(k for k,_ in itertools.groupby(all_infections)) #remove dubplicats

    combinations = len(all_infections)
    print (all_infections)
    
    resoults = []

    for index in range(combinations): #calculate the infected states
        resoults = resoults + [grid_infecter(all_infections[index],n)]
        
    print(resoults)




def grid_infecter(grid, n):
    
    servers = n*n
    new_grid = []
    
    
    while new_grid != grid:

        for index in range(servers):

            if grid[index] == 2:

                if index % n != 0:     #infect left
                    grid[index - 1] += 1
                    
                if ((index - 1) % n != 0 or index == 0) and index != servers - 1: #infect right
                    grid[index + 1] += 1
                    
                if index < (n**2 - n): #infect down
                    grid[index + n] += 1
                    
                if index > (n - 1): #infect up
                    grid[index - n] += 1
            new_grid = grid


    total_infections = sum([a for a in new_grid if a == 2])//2
    print(new_grid, "Total infections: " , total_infections)
    
    if len(grid)> 0 and len(grid) == 2*sum(grid):
        return True
    else:
        return False



    
