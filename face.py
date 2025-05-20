class Face:
    def __init__(self, row0=[], row1=[], row2=[], val=''):
        if row0 == [] and row1 == [] and row2 == []:
            row0 = [val, val, val]
            row1 = [val, val, val]
            row2 = [val, val, val]

        self.face = [row0, row1, row2]

    def get_row(self, index):
        return self.face[index]

    def get_column(self, index):
        return [self.face[0][index], self.face[1][index], self.face[2][index]]

    def get_face(self):
        return self.face

    def set_face(self, face: []):
        self.face = face

    def set_row(self, index, vals):
        self.face[index] = vals

    def set_column(self, index, vals):
        for i in range(3):
            self.face[i][index] = vals[i]

    def turn_left(self):

        old_face = self.face.copy()

        self.set_row(0, [old_face[0][2], old_face[1][2], old_face[2][2]])
        self.set_row(1, [old_face[0][1], old_face[1][1], old_face[2][1]])
        self.set_row(2, [old_face[0][0], old_face[1][0], old_face[2][0]])

    def turn_right(self):
        for i in range(3):
            self.turn_left()

    def turn_two(self):
        for i in range(2):
            self.turn_left()

    def print_face(self):
        print(self.face[0])
        print(self.face[1])
        print(self.face[2])