from lib.models import Coord, MarsRover, Grid, Direction
from lib.mars_rover import move_one, turn, run

def test_moves_forwards():
    start_coord = Coord(1, 1)
    directions_and_expected_coords = [("N", Coord(1, 2)), ("S", Coord(1, 0)), ("E", Coord(2, 1)), ("W", Coord(0, 1))]
    for (direction, expected_coord) in directions_and_expected_coords:
        mars_rover = MarsRover(start_coord, direction)
        end_rover = move_one(mars_rover, reverse=False, grid=Grid(10, 10))
        assert(end_rover.coord) == expected_coord


def test_moves_backwards():
    start_coord = Coord(1, 1)
    directions_and_expected_coords = [("N", Coord(1, 0)), ("S", Coord(1, 2)), ("E", Coord(0, 1)), ("W", Coord(2, 1))]
    for (direction, expected_coord) in directions_and_expected_coords:
        mars_rover = MarsRover(start_coord, direction)
        end_rover = move_one(mars_rover, reverse=True, grid = Grid(10, 10))
        assert(end_rover.coord) == expected_coord

def test_wraps_around_if_move_takes_off_of_grid():
    grid = Grid(10, 8)
    mars_rover_to_expected_end = [
        (MarsRover(Coord(9, grid.y_max), "N"), Coord(9, 0)),
        (MarsRover(Coord(9, 0), "S"),          Coord(9, grid.y_max)),
        (MarsRover(Coord(grid.x_max, 6), "E"), Coord(0, 6)),
        (MarsRover(Coord(0, 6), "W"),          Coord(grid.x_max, 6))
        ]
    for (mars_rover, expected_end_coord) in mars_rover_to_expected_end:
        end_rover = move_one(mars_rover, reverse=False, grid = grid)
        assert(end_rover.coord) == expected_end_coord

def test_turns_right():
    directions_to_expected_directions = [("N", "E"), ("E", "S"), ("S", "W"), ("W", "N")]
    for (direction, expected_direction) in directions_to_expected_directions:
        mars_rover = MarsRover(Coord(0, 0), direction)
        end_rover = turn(mars_rover, clockwise=True)
        assert(end_rover.direction) == expected_direction

def test_turns_left():
    directions_to_expected_directions = [("N", "W"), ("W", "S"), ("S", "E"), ("E", "N")]
    for (direction, expected_direction) in directions_to_expected_directions:
        mars_rover = MarsRover(Coord(0, 0), direction)
        end_rover = turn(mars_rover, clockwise=False)
        assert(end_rover.direction) == expected_direction

def test_runs_a_list_of_commands():
    commands = ["f", "f", "r", "f", "l", "b", "f", "f", "r", "b", "b"]
    grid = Grid(10, 10)
    start_rover = MarsRover(Coord(0, 0), "N")
    expected_end_coord = Coord(10, 3)
    expected_end_direction = "E"
    expected_success_status = True
    (end_rover, mission_success) = run(commands, start_rover, grid, [])
    assert(end_rover.coord) == expected_end_coord
    assert(end_rover.direction) == expected_end_direction
    assert(mission_success) == expected_success_status

def test_aborts_path_and_reports_if_obstacle_is_encountered():
    start_coord = Coord(0, 0)
    start_dir = "N"
    obstacles = [Coord(1, 1)]
    commands = ["f", "r", "f", "f", "f", "l"]
    expected_end_coord = Coord(0, 1)
    expected_end_dir = "E"
    expected_success_status = False
    (end_rover, mission_success) = run(commands, MarsRover(start_coord, start_dir), Grid(10, 10), obstacles)
    assert(end_rover.coord) == expected_end_coord
    assert(end_rover.direction) == expected_end_dir
    assert(mission_success) == expected_success_status

