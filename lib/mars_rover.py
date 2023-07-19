from lib.models import MarsRover, Coord, Grid, update_mars_rover_coord, update_mars_rover_direction
from typing import List

def move_one(mars_rover: MarsRover, reverse: bool, grid: Grid) -> MarsRover:
    directions_to_deltas = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
    (x_delta, y_delta) = directions_to_deltas[mars_rover.direction]
    if reverse:
        return update_mars_rover_coord(mars_rover, x_delta * -1, y_delta * -1, grid)
    else:
        return update_mars_rover_coord(mars_rover, x_delta, y_delta, grid)

def turn(mars_rover: MarsRover, clockwise: bool) -> MarsRover:
    directions_list = ["N", "E", "S", "W"]
    current_direction_index = directions_list.index(mars_rover.direction)
    next = current_direction_index + 1 if clockwise else current_direction_index - 1
    return update_mars_rover_direction(mars_rover, directions_list[next % len(directions_list)])

def run(commands: List[str], rover: MarsRover, grid: Grid, obstacles: List[Coord]) -> tuple[MarsRover, bool]:
    if len(commands) == 0:
        return (rover, True)
    else:
        first_command, *remaining_commands = commands
        transformation_function = {
            "l": lambda rover: turn(rover, False), 
            "r": lambda rover: turn(rover, True), 
            "f": lambda rover: move_one(rover, False, grid),
            "b": lambda rover: move_one(rover, True, grid)
        }[first_command]
        new_rover = transformation_function(rover)
        if new_rover.coord in obstacles:
            return (rover, False)
        else:
            return run(remaining_commands, new_rover, grid, obstacles)
