from dataclasses import dataclass, replace
from enum import Enum


@dataclass(frozen=True)
class Coord:
    x: int
    y: int


Direction = Enum('Direction', ['N', 'S', 'E', 'W'])


@dataclass(frozen=True)
class MarsRover:
    coord: Coord
    direction: Direction


@dataclass(frozen=True)
class Grid:
    x_max: int
    y_max: int


def update_mars_rover_coord(mars_rover: MarsRover, x_by: int, y_by: int, grid: Grid) -> MarsRover:
    new_y = (mars_rover.coord.y + y_by) % (grid.y_max + 1)
    new_x = (mars_rover.coord.x + x_by) % (grid.x_max + 1)
    return replace(mars_rover, coord=replace(mars_rover.coord, x=new_x, y=new_y))


def update_mars_rover_direction(mars_rover: MarsRover, new_direction: Direction) -> MarsRover:
    return replace(mars_rover, direction=new_direction)
