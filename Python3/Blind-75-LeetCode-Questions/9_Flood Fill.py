# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Time Complexity : O(n*m)
# Space Complexity : O(n*m)
class Solution:
    def fill(self, image, sr, sc, color, current):
        # check if sr, sc not in range of index
        if not (0 <= sr < len(image)) or not (0 <= sc < len(image[0])):   return

        # check if not connected to last one (find the part of connected area)
        if current != image[sr][sc]:    return
        image[sr][sc] = color

        self.fill(image, sr - 1, sc, color, current)
        self.fill(image, sr + 1, sc, color, current)
        self.fill(image, sr, sc - 1, color, current)
        self.fill(image, sr, sc + 1, color, current)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # if target and color, no need to adjust
        if image[sr][sc] == color:  return image
        self.fill(image, sr, sc, color, image[sr][sc])
        return image