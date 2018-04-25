
class Map(object):

    def __init__(self, map_matrix, side_len):
        self.row = len(map_matrix)
        self.col = len(map_matrix[0])
        self.side_len = side_len

    def getScreenWidth(self):
        return self.col * self.side_len

    def getScreenHeight(self):
        return self.row * self.side_len

    def num2pixel(self, num):
        return int(num * self.side_len - self.side_len/2)

    def pixel2num(self, pixel):
        return int(pixel / self.side_len)


