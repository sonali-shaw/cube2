import cube

class Tester:
    def __init__(self, cube1 : cube.Cube):
        self.cube = cube1

        # initialize to a given state
        self.reset()

    def reset(self):
        self.cube.front_face.set_face([['y', 'y', 'y'], ['r', 'w', 'r'], ['y', 'b', 'g']])
        self.cube.left_face.set_face([['r', 'w', 'b'], ['o', 'b', 'w'], ['o', 'o', 'b']])
        self.cube.right_face.set_face([['g', 'y', 'o'], ['g', 'g', 'b'], ['r', 'b', 'w']])
        self.cube.post_face.set_face([['w', 'g', 'w'], ['y', 'y', 'g'], ['r', 'y', 'g']])
        self.cube.top_face.set_face([['b', 'w', 'b'], ['b', 'r', 'r'], ['o', 'o', 'o']])
        self.cube.bottom_face.set_face([['r', 'r', 'y'], ['w', 'o', 'o'], ['w', 'g', 'g']])

    def printer(self, str1, str2):
        print("Current state: " + str1)
        print("Desired state: " + str2)
        print(f"Differences at indices: {self.get_diff_indices(str1, str2)}")

    def test_inverses(self):

        moves = ['f+', 'f-', 'l+', "l-", "r+", "r-", "b+", "b-", "t+", "t-", "p+", "p-"]
        moves2 = ['f2', 'l2', 'r2', 'b2', 't2', 'p2']

        # test counter-clockwise and clockwise motion are inverses
        for i in range(0, len(moves), 2):
            move1 = moves[i]
            move2 = moves[i+1]
            state1 = self.cube.get_str_state()
            self.cube.move(move1)
            self.cube.move(move2)
            if state1 != self.cube.get_str_state():
                raise AssertionError(f"{move1} and {move2} are not inverses")
            self.reset()

        # test that moving x2 twice has no net change
        for i in range(len(moves2)):
            move = moves2[i]
            state1 = self.cube.get_str_state()
            self.cube.move(move)
            self.cube.move(move)
            if state1 != self.cube.get_str_state():
                raise AssertionError(f"{move} twice has a net change")
            self.reset()

    def test_moves(self):

        # test all moves
        self.cube.move('f+')
        current_state = self.cube.get_str_state()
        desired_state = 'yrybwygry rwrobrooy oyoogbobw wgwyygryg bwbbrrbwb rggwoowgg'
        if (current_state != desired_state):
            self.printer(current_state, desired_state)
            raise AssertionError("f+ not working as intended")
        self.reset()

        self.cube.move('f-')
        current_state = self.cube.get_str_state()
        desired_state = 'yrgywbyry rwooboooo yyorgbrbw wgwyygryg bwbbrrggr bwbwoowgg'
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("f- not working as intended")
        self.reset()

        self.cube.move('f2')
        current_state = self.cube.get_str_state()
        desired_state = 'gbyrwryyy rwrobgoog byowgbbbw wgwyygryg bwbbrryrr ooowoowgg'
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("f2 not working as intended")
        self.reset()

        self.cube.move('l+')
        current_state = self.cube.get_str_state()
        desired_state = 'byybwrobg oorobwbwb gyoggbrbw wgwyywryr gwbgrrwoo yryrooygg'
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("l+ not working as intended")
        self.reset()

        self.cube.move('l-')
        current_state = self.cube.get_str_state()
        desired_state = "ryywwrwbg bwbwboroo gyoggbrbw wgoyybryb ywbrrryoo grygoowgg"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("l- not working as intended")
        self.reset()

        self.cube.move('l2')
        current_state = self.cube.get_str_state()
        desired_state = 'gyygwrwbg boowbobwr gyoggbrbw wgyyyrryy rwbwrrwoo brybooogg'
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("l2 not working as intended")
        self.reset()

        self.cube.move('r+')
        current_state = self.cube.get_str_state()
        desired_state = "yyyrwoybg rwbobwoob rggbgywbo ogwrygbyg bwybrroog rrrwoywgw"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("r+ not working as intended")
        self.reset()

        self.cube.move('r-')
        current_state = self.cube.get_str_state()
        desired_state = "yybrwrybo rwbobwoob obwygbggr ggwoygyyg bwrbryoow rryworwgg"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("r- not working as intended")
        self.reset()

        self.cube.move('r2')
        current_state = self.cube.get_str_state()
        desired_state = "yyrrwyybw rwbobwoob wbrbggoyg ggwrygyyg bwybrooog rrbworwgo"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("r2 not working as intended")
        self.reset()

        self.cube.move('b+')
        current_state = self.cube.get_str_state()
        desired_state = "yyyrwroob rwbobwryg gyoggbybg wgwyygrbw bwbbrrooo wwrgorgoy"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("b+ not working as intended")
        self.reset()

        self.cube.move('b-')
        current_state = self.cube.get_str_state()
        desired_state = "yyyrwrrbw rwbobwybg gyoggbryg wgwyygoob bwbbrrooo yogrogrww"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("b- not working as intended")
        self.reset()

        self.cube.move("b2")
        current_state = self.cube.get_str_state()
        desired_state = "yyyrwrryg rwbobwrbw gyoggboob wgwyygybg bwbbrrooo ggwoowyrr"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("b2 not working as intended")
        self.reset()

        self.cube.move("t+")
        current_state = self.cube.get_str_state()
        desired_state = "gyorwrybg yyyobwoob wgwggbrbw rwbyygryg obborworb rrywoowgg"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("t+ not working as intended")
        self.reset()

        self.cube.move("t-")
        current_state = self.cube.get_str_state()
        desired_state = "rwbrwrybg wgwobwoob yyyggbrbw gyoyygryg browrobbo rrywoowgg"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("t- not working as intended")
        self.reset()

        self.cube.move("t2")
        current_state = self.cube.get_str_state()
        desired_state = "wgwrwrybg gyoobwoob rwbggbrbw yyyyygryg ooorrbbwb rrywoowgg"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("t2 not working as intended")
        self.reset()

        self.cube.move("p+")
        current_state = self.cube.get_str_state()
        desired_state = "yyyrwrybg bwbwbwbob gyggggrbw rywyygggw obwbrrooo rrywooroo"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("p+ not working as intended")
        self.reset()

        self.cube.move("p-")
        current_state = self.cube.get_str_state()
        desired_state = "yyyrwrybg wwbgbwgob gybggwrbb wgggyywyr oorbrrooo rrywoowbo"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("p- not working as intended")
        self.reset()

        self.cube.move("p2")
        current_state = self.cube.get_str_state()
        desired_state = "yyyrwrybg wwbbbwoob gyoggorbr gyrgyywgw ggwbrrooo rrywoobwb"
        if current_state != desired_state:
            self.printer(current_state, desired_state)
            raise AssertionError("p- not working as intended")
        self.reset()

    def test_all(self):
        self.test_inverses()
        self.test_moves()

    def get_diff_indices(self, str1, str2):
        indices = []

        if (str1 == str2) or (len(str1) != len(str2)):
            return []

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                indices.append(i)

        return indices

cube1 = cube.Cube()
tester = Tester(cube1)
tester.test_all()