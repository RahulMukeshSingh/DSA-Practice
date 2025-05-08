def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color: return image
        start_color = image[sr][sc]
        def dfs(x,y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            if image[x][y] == color or image[x][y] != start_color: return
            image[x][y]=color
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
        dfs(sr,sc) 
        return image