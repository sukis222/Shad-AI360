class LifeGame(object):
    """
    Class for Game life
    """

    def __init__(self, lst: list[list[int]]) -> None:
        self.ocean = [[0 for i in range(len(lst[0]) + 2)] for j in range(len(lst) + 2)]
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                self.ocean[i + 1][j + 1] = lst[i][j]


    def get_next_generation(self) -> list[list[int]]:

        new_one = [[self.ocean[j][i] for i in range(len(self.ocean[j]))] for j in range(len(self.ocean))]
        hills = [[0 for i in range(len(self.ocean[0]))] for j in range(len(self.ocean))]
        shrimps = [[0 for i in range(len(self.ocean[0]))] for j in range(len(self.ocean))]
        fishes = [[0 for i in range(len(self.ocean[0]))] for j in range(len(self.ocean))]

        for i in range(len(self.ocean) - 2):
            for j in range(len(self.ocean[0]) - 2):
                if self.ocean[i + 1][j + 1] == 1:
                    hills[i+1][j+1] = 1
                if self.ocean[i + 1][j + 1] == 2:
                    fishes[i+1][j+1] = 1
                if self.ocean[i + 1][j + 1] == 3:
                    shrimps[i+1][j+1] = 1

        for i in range(len(self.ocean) - 2):
            for j in range(len(self.ocean[0]) - 2):
                ribki = (fishes[i + 1][j + 2] + fishes[i][j] + fishes[i][j + 1] + fishes[i][j + 2] + fishes[i + 1][j] +
                         fishes[i + 2][j + 2] + fishes[i + 2][j] + fishes[i + 2][j + 1])
                krivetki = (shrimps[i + 1][j + 2] + shrimps[i][j] + shrimps[i][j + 1] + shrimps[i][j + 2] +
                            shrimps[i + 1][j] +
                            shrimps[i + 2][j + 2] + shrimps[i + 2][j] + shrimps[i + 2][j + 1])
                if self.ocean[i + 1][j + 1] == 2:
                    if ribki <= 1 or ribki >= 4:
                        new_one[i+1][j+1] = 0


                if self.ocean[i + 1][j + 1] == 3:
                    if krivetki <= 1 or krivetki >= 4:
                        new_one[i+1][j+1] = 0

                if self.ocean[i + 1][j + 1] == 0:
                    if ribki == 3:
                        new_one[i+1][j+1] = 2
                    elif krivetki == 3:
                        new_one[i + 1][j + 1] = 3

        self.ocean = new_one
        return [[self.ocean[j][i] for i in range(1, len(self.ocean[j]) - 1)] for j in range(1, len(self.ocean) - 1)]

    def __fcs(self) -> None:
        pass

