# Julio Claros
# 114153234
# 2018-05-11
# Exercise


class ChessPiece:

    def __init__(self, name, color, rank, file):
        self.name = name
        self.color = color
        self.rank = rank
        self.file = file

    def position(self):
        return self.file, self.rank

    def move(self, new_file, new_rank):
        self.file = new_file
        self.rank = new_rank

    def possible_moves(self):
        raise NotImplementedError


class King(ChessPiece):

    def __init__(self, color, file, rank):
        ChessPiece.__init__(self, name="King", color=color, file=file,
                            rank=rank)

    def possible_moves(self):
        moves = []
        for x in [-1, 0, 1]:
            new_file = self.file + x
            if not (0 < new_file < 9):
                continue
            for y in [-1, 0, 1]:
                new_rank = self.rank + y
                if not(0 < new_rank < 9):
                    continue
                    moves.append(new_file, new_rank)
        return moves