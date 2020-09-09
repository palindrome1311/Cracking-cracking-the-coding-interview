#leet code flood fill
#https://leetcode.com/problems/flood-fill/
def flood(oc,nc,image,r,c):
    if(r<0 or c<0 or image[r][c]==nc):
        return
    image[r][c]=nc
    rows=len(image)
    cols=len(image[0])
    if(r+1<rows and image[r+1][c]==oc):
        flood(oc,nc,image,r+1,c)
    if(r-1>-1 and image[r-1][c]==oc ):
        flood(oc,nc,image,r-1,c)
    if(c+1<cols and image[r][c+1]==oc ):
        flood(oc,nc,image,r,c+1)
    if(c-1>-1 and image[r][c-1]==oc ):
        flood(oc,nc,image,r,c-1)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        flood(image[sr][sc],newColor,image,sr,sc)
        return image
        
        