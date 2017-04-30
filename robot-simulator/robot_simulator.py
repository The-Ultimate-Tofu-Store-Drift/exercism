
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):

    def __init__(self, direction=NORTH, x_position=0, y_position=0):
        self.coordinates = (x_position, y_position)
        self.bearing = direction    # self.bearings[direction]

    bearings = {
        0: "NORTH",
        1: "EAST",
        2: "SOUTH",
        3: "WEST"
    }

    def turn_right(self):
        self.bearing += 1

        if self.bearing > 3:
            self.bearing = 0

    def turn_left(self):
        self.bearing -= 1

        if self.bearing < 0:
            self.bearing = 3

    def advance(self):

        if self.bearing == 0:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)

        elif self.bearing == 1:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])

        elif self.bearing == 2:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)

        elif self.bearing == 3:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])


if __name__ == "__main__":
    robot = Robot()
    robot.advance()
    print(robot.coordinates, robot.bearing)
