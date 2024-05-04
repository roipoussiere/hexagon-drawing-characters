# Hexagon-drawing characters

A monospace characters set designed to draw hexagonal characters, that can be used in flat files or a terminal.

It aims to be the equivalent of the [box-drawing characters](https://en.wikipedia.org/wiki/Box_Drawing) for hexagons. Like this last, the hexagon-drawing characters are designed with 3 line styles: *light*, *heavy* and *double*.

## Large Flat-top Hexagon Drawings

This set is composed of 11 shapes:
- 1 horizontal bar;
- 6 corners;
- 2 forks used to connect hexagons;
- 2 diagonal bars used to extend the hexagons in order to get bigger ones.

The smallest hexagon in this set can be drawn on a 5x3 grid.

It contains 3 free slots in the center, that can be used to include any other monospace character.

### Examples of use

#### Minimal hexagon

![](./images/examples/large_flat_top_simple.png)

#### Extended hexagon

![](./images/examples/large_flat_top_extended.png)

#### Hexagonal tiling

![](./images/examples/large_flat_top_tiling.png)

### Representation

#### Light

*Coming soon*

#### Heavy

| image | name | note |
|-------|------|------|
| **Lines** |||
| ![](images/chars/large_flat_top/heavy_straight_line_horizontal.png) | heavy straight line horizontal | similar to `━`: `\u2501` - Box Drawings Heavy Horizontal |
| ![](images/chars/large_flat_top/heavy_diagonal_falling.png) | heavy diagonal falling | |
| ![](images/chars/large_flat_top/heavy_diagonal_rising.png) | heavy diagonal rising | |
| **Corners** |||
| ![](images/chars/large_flat_top/heavy_corner_lower_left.png) | heavy corner lower left | |
| ![](images/chars/large_flat_top/heavy_corner_lower_right.png) | heavy corner lower right | |
| ![](images/chars/large_flat_top/heavy_corner_left.png) | heavy corner left | |
| ![](images/chars/large_flat_top/heavy_corner_right.png) | heavy corner right | |
| ![](images/chars/large_flat_top/heavy_corner_upper_left.png) | heavy corner upper left | |
| ![](images/chars/large_flat_top/heavy_corner_upper_right.png) | heavy corner upper right | |
| **Forks** |||
| ![](images/chars/large_flat_top/heavy_fork_left.png) | heavy fork left | |
| ![](images/chars/large_flat_top/heavy_fork_right.png) | heavy fork right | |

#### Double

*Coming soon*

### Construction

![](images/construction/large_flat_top.png)

*Each crosshair is located on the center of its surrouding box.*

## Large Pointy-top Hexagon Drawings

This set is composed of 15 shapes:
- 1 vertical bar;
- 6 corners;
- 2 forks;
- 2 centered diagonal bars;
- 4 shifted diagonal bars, used to extend the hexagons in order to get bigger ones.

Like in the flat-top set, the smallest hexagon in this set can be drawn on a 5x3 grid.

It also contains 3 free slots in the center, that can be used to include any other monospace character.

### Construction

Each crosshair is located on the center of its surrouding box.

### Representation

#### Light

*Coming soon*

#### Heavy

Characters representation, examples and construction:

![](schematics/exports/png/large_pointy_top.png)

The vertical bar is supposed to be similar to `┃` (`\u2503`: Box Drawings Heavy Vertical)

#### Double

*Coming soon*

## Small flat-top hexagons

*Coming soon*

## Small pointy-top hexagons

*Coming soon*
