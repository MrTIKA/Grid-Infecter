### Fun for CS 131
import itertools
import sys



def grid_maker(n): 

    servers = n*n   #number of servers
    infected = n - 1 #number of infected servers
    grid = [ 0 for a in range(servers)] #list representing grid, with all servers uninfected
    grid = grid[:-infected] + infected * [2] #infect last servests in grid

    lenght = len(grid)

    all_infections = unique_permutations(grid)
    all_infections = list(all_infections)
    
    combinations = len(all_infections)
##    print(all_infections)
    
    resoult = False

    for element in all_infections: #calculate the infected states
       resoult = resoult or grid_infecter(element ,n, lenght)
        
    return resoult




def grid_infecter(grid, n, lenght):
    
    servers = n*n
    new_grid = []
    lenght = lenght

    
    
    while new_grid != grid:

        for index in range(servers):

            if grid[index] == 2:

                if index % n != 0:      #infect left
                    grid[index - 1] += 1
                    
                if ((index - 1) % n != 0 or index == 0) and index != servers - 1: #infect right
                    grid[index + 1] += 1
                    
                if index < (n**2 - n):   #infect down
                    grid[index + n] += 1
                    
                if index > (n - 1):      #infect up
                    grid[index - n] += 1
            new_grid = grid


    total_infections = sum([a for a in new_grid if a == 2])//2
  


    
##    if lenght == 2*sum(grid):
##        return True
##    else:
##        return False



    return checkEqual3(grid)


    
def unique_permutations(t):
    lt = list(t)
    lnt = len(lt)
    if lnt == 1:
        yield lt
    st = set(t)
    for d in st:
        lt.remove(d)
        for perm in unique_permutations(lt):
            yield [d]+perm
        lt.append(d)

def checkEqual3(lst):
       return lst[1:] == lst[:-1]
