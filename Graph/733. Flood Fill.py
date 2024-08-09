class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        
        def fill(i, j, original):
            if i < 0 or j < 0 or i >= R or j >= C or image[i][j] != original:
                return
            image[i][j] = color
            fill(i - 1, j, original)
            fill(i + 1, j, original)
            fill(i, j - 1, original)            
            fill(i, j + 1, original)            
            
        if image[sr][sc] == color:
            return image                    
        fill(sr, sc, image[sr][sc])
        return image