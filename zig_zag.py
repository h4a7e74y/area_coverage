def unique(list1): 
    unique_list = []
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x)
    return unique_list


    
    
    
def convert_coordinates(a):
    a=np.array(a)
    x,y=[],[]
    for b in a:
        x.append(b[0])
        y.append(b[1])
    return x,y
    
def get_grid_size(a):
    x,y = convert_coordinates(a)
    return len(unique(x)), len(unique(y))
    
def get_zigzag_path(grid):
    X_DIM, Y_DIM =get_grid_size(grid)
    
    x,y=convert_coordinates(grid)
        
    min_x=min(x)
    max_x=max(x)

    min_y=min(y)
    max_y=max(y)

    nx=np.linspace(min_x,max_x,X_DIM)
    ny=np.linspace(min_y,max_y,Y_DIM)
    zr=np.meshgrid(nx,ny)
    
    new_coords=[]
    coord=()
    counter=0

    for i in range(Y_DIM):
        for j in range(X_DIM):

            for g in range(len(grid)):
                if i%2==0:
                    nj=j
                else:
                    nj=X_DIM-j-1

                if (grid[g][0] == int(zr[0][i][nj])) and (grid[g][1] == int(zr[1][i][nj])):
                    coord=[int(zr[0][i][nj]),int(zr[1][i][nj])]
                    #coord=[a[g][0],a[g][1]]
                    new_coords.append(coord)
                    coord=[]
                counter+=1
      
    print(get_grid_size(grid))
    return new_coords



def get_waypoints(field, grid, drones_inits,step):
    #print(grid)
    z=get_zigzag_path(grid)
    #print(grid)
    a=z[len(z)//2:]
    b=z[:len(z)//2]
    print(a)
    print(b)
    a = [drones_inits[0]]*40+find_way_to(drones_inits[0],a[0],grid,step)+a[:-1]+find_way_to(a[-1],drones_inits[0],grid,step)
    b = find_way_to(drones_inits[1],b[0],grid,step)+b[:-1]+find_way_to(b[-1],drones_inits[1],grid,step)
    print(a)
    print(b)
    print(grid)
    return [   
        a,b
    ]

def check_waypoints(a,b):
    for i in range(len(a)):
        for b in range(len(b)):
            pass
            print()

def distance(x,y):
    return (x**2+y**2)**0.5

def find_way_to(cur_p, des_p, grid, step):
    new_a=[cur_p]
    temp=[]
    tempi=[]
    i=0
    
    while True:
        for z in grid:
            if (abs(z[0]-new_a[-1][0])<=step) and (abs(z[1]-new_a[-1][1])<=step) and (distance(des_p[0]-z[0],des_p[1]-z[1]) < distance(des_p[0]-new_a[-1][0],des_p[1]-new_a[-1][1])):
                #print(z)
                temp.append(z)
                tempi.append(distance(des_p[0]-z[0],des_p[1]-z[1]))
        #print(temp)
        #print(tempi)
        #print('*'*5)
        
        if temp==[]:
            break
        new_a.append(temp[tempi.index(min(tempi))])
        temp=[]
        tempi=[]
        i+=1
        if i>len(grid):
            break
        
    #print(i)
    if new_a[-1]!=des_p:
        new_a+=[des_p]
    return new_a
