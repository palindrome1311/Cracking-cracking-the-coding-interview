def getpath(mat):
    path=[]
    visited=set()
    rows = len(mat)-1
    cols= len(mat[0])-1
    if(isValid(mat,rows,cols,path,visited)):
        return path
    return None

def isValid(mat,rows,cols,path,visited):
    #out of bounds check or obstacle check
    if(cols < 0 or rows < 0 or not mat[rows][cols]):
        return False
    
    point = (rows,cols)

    if(point in visited):
        return False
    print(point)
    atOrigin = (rows==0) or (cols==0)

    if(isValid(mat,rows - 1,cols, path,visited) or isValid(mat,rows,cols - 1, path,visited) or  atOrigin ):
        path.append(point)
        return True
    
    visited.add(point)
    return False



mat =  [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ], 
        [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],  
        [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],  
        [ 1, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],  
        [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],  
        [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],  
        [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],  
        [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],  
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]] 


#top left to bottom right
print(getpath(mat))
