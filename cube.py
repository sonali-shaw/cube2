import face
import random

class Cube:

    def __init__(self,
                 front = [],
                 left = [],
                 right = [],
                 post = [],
                 top = [],
                 bottom = [],
                 scramble = False,
                 scramble_num = 25):

        # create presolved cube
        sum_lens = len(front) + len(left) + len(right) + len(post) + len(top) + len(bottom)
        if sum_lens == 0:
            self.front_face = face.Face(val='w')
            self.left_face = face.Face(val='g')
            self.right_face = face.Face(val='b')
            self.post_face = face.Face(val='y')
            self.top_face = face.Face(val='o')
            self.bottom_face = face.Face(val='r')

        if scramble:
            self.scramble(scramble_num)

        # given specific values for each face
        # note: to do this the user should pass in faces to each of the parameters
        if type(front) == face.Face:
            self.front_face = front
            self.left_face = left
            self.right_face = right
            self.post_face = post
            self.top_face = top
            self.bottom_face = bottom

    def print_cube(self):
        print("Cube state:")

        print("--------------------")
        print("front:")
        self.front_face.print_face()

        print("--------------------")
        print("left:")
        self.left_face.print_face()

        print("--------------------")
        print("right: ")
        self.right_face.print_face()

        print("--------------------")
        print("post: ")
        self.post_face.print_face()

        print("--------------------")
        print("top: ")
        self.top_face.print_face()

        print("--------------------")
        print("bottom: ")
        self.bottom_face.print_face()

    def get_state(self):
        return [
            self.front_face.get_face(),
            self.left_face.get_face(),
            self.right_face.get_face(),
            self.post_face.get_face(),
            self.top_face.get_face(),
            self.bottom_face.get_face()
        ]

    # returns the 54 characters as a concatenated string
    def get_str_state(self):

        string_state = ""
        faces = [self.front_face, self.left_face, self.right_face, self.post_face, self.top_face, self.bottom_face]

        for face in faces:
            for row in face.get_face():
                for value in row:
                     string_state += value
            string_state += " "

        return string_state[:-1]

    # turns: makes the given side the front side
    def turn_right(self):

        old_front = self.front_face.get_face()
        old_post = self.post_face.get_face()
        old_left = self.left_face.get_face()
        old_right = self.right_face.get_face()

        self.front_face.set_face(old_right)
        self.right_face.set_face(old_post)
        self.post_face.set_face(old_left)
        self.left_face.set_face(old_front)

        self.top_face.turn_right()
        self.bottom_face.turn_left()

    def turn_left(self):
        self.turn_right()
        self.turn_right()
        self.turn_right()

    def turn_up(self):

        old_front = self.front_face.get_face()
        old_top = self.top_face.get_face()
        old_bottom = self.bottom_face.get_face()
        old_post = self.post_face.get_face()

        self.front_face.set_face(old_bottom)
        self.top_face.set_face(old_front)
        self.post_face.set_face(old_top)
        self.post_face.turn_two()
        self.bottom_face.set_face(old_post)

        self.left_face.turn_left()
        self.right_face.turn_right()
        self.bottom_face.turn_two()

    def turn_down(self):

        self.turn_up()
        self.turn_up()
        self.turn_up()

    def turn_two(self):
        self.turn_left()
        self.turn_left()

    def opposite_direction(self, direction):
        opposites = {"+": "-", "2": "2", "-": "+"}
        return opposites[direction]

    def turn_side_helper(self):

        top_row2 = self.top_face.get_row(2)
        left_col2 = self.left_face.get_column(2)
        bottom_row0 = self.bottom_face.get_row(0)
        right_col0 = self.right_face.get_column(0)

        bottom_row0.reverse()
        top_row2.reverse()

        self.front_face.turn_left()
        self.left_face.set_column(2, top_row2)
        self.bottom_face.set_row(0, left_col2)
        self.right_face.set_column(0, bottom_row0)
        self.top_face.set_row(2, right_col0)

    def turn_side(self, direction):
        # turns the front side
        direction_num = {'-': 1, '2': 2, '+': 3}
        for i in range(direction_num[direction]):
            self.turn_side_helper()

    def move(self, move):
        face = move[0]
        direction = move[1]
        if face == 'r':
            self.turn_right()
            self.turn_side(direction)
            self.turn_left()
        elif face == 'f':
            self.turn_side(direction)
        elif face == 'l':
            self.turn_left()
            self.turn_side(direction)
            self.turn_right()
        elif face == 'b':
            self.turn_up()
            self.turn_side(direction)
            self.turn_down()
        elif face == 't':
            self.turn_down()
            self.turn_side(direction)
            self.turn_up()
        elif face == 'p':
            self.turn_two()
            self.turn_side(direction)
            self.turn_two()

    def is_won(self):
        faces = [self.front_face, self.left_face, self.right_face, self.post_face, self.top_face, self.bottom_face]
        for face in faces:
            for row in face.get_face():
                for value in row:
                    if value != face.get_row(0)[0]:
                        return False
        return True

    def scramble(self, num_moves=25):
        moves = ['f+', 'f-', 'f2', 'l+', "l-", 'l2', "r+", "r-", 'r2', "b+", "b-", 'b2', "t+", "t-", 't2', "p+", "p-", 'p2']
        archive = []

        for _ in range(num_moves):

            rand_int = random.randint(0, len(moves) - 1)
            self.move(moves[rand_int])

            archive.append(moves[rand_int])

        return archive

# cube1 = Cube()
# record = cube1.scramble(3)
#
# print(record)
# cube1.print_cube()


