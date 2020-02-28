def dirReduc(arr):
    # dic = {('NORTH','SOUTH'), ('SOUTH','NORTH'), ('WEST','EAST'), ('EAST','WEST')}
    # cnt = 1
    # while cnt > 0:
    #     cnt = 0
    #     for i in range(len(arr) -1):
    #         if (arr[i], arr[i + 1]) in dic:
    #             del arr[i + 1]
    #             del arr[i]
    #             cnt += 1
    #             break
    # return arr
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr    
            
            


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])