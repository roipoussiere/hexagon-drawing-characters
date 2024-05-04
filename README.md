# Hexagon-drawing characters

A monospace character set designed to draw hexagonal characters, that can be used in flat files or a terminal.

It aims to be the equivalent of the [box-drawing characters](https://en.wikipedia.org/wiki/Box_Drawing) for hexagons. This set is designed with 2 line styles: *simple* and *double*, and allow mixing both.

## Large Flat-top Hexagon Drawings

The smallest hexagon in this set can be drawn on a 5x3 grid. It contains 3 free slots in the center, that can be used to include any other monospace character.

### Character set

#### Simple lines (11 chars)

![](images/chars/large_flat_top/simple_straight_line_horizontal.png)
![](images/chars/large_flat_top/simple_corner_lower_left.png)
![](images/chars/large_flat_top/simple_corner_lower_right.png)
![](images/chars/large_flat_top/simple_corner_upper_left.png)
![](images/chars/large_flat_top/simple_corner_upper_right.png)
![](images/chars/large_flat_top/simple_corner_left.png)
![](images/chars/large_flat_top/simple_corner_right.png)
![](images/chars/large_flat_top/simple_fork_right.png)
![](images/chars/large_flat_top/simple_fork_left.png)
![](images/chars/large_flat_top/simple_diagonal_rising.png)
![](images/chars/large_flat_top/simple_diagonal_falling.png)

![](./images/examples/large_flat_top_simple.png)

#### Double lines (11 chars)

![](images/chars/large_flat_top/double_straight_line_horizontal.png)
![](images/chars/large_flat_top/double_corner_lower_left.png)
![](images/chars/large_flat_top/double_corner_lower_right.png)
![](images/chars/large_flat_top/double_corner_upper_left.png)
![](images/chars/large_flat_top/double_corner_upper_right.png)
![](images/chars/large_flat_top/double_corner_left.png)
![](images/chars/large_flat_top/double_corner_right.png)
![](images/chars/large_flat_top/double_fork_right.png)
![](images/chars/large_flat_top/double_fork_left.png)
![](images/chars/large_flat_top/double_diagonal_rising.png)
![](images/chars/large_flat_top/double_diagonal_falling.png)

![](./images/examples/large_flat_top_double.png)

#### Mixed (12 chars)

![](images/chars/large_flat_top/simple_fork_right_double_lower_right.png)
![](images/chars/large_flat_top/double_fork_right_simple_left.png)
![](images/chars/large_flat_top/simple_fork_right_double_left.png)
![](images/chars/large_flat_top/double_fork_right_simple_upper_right.png)
![](images/chars/large_flat_top/simple_fork_right_double_upper_right.png)
![](images/chars/large_flat_top/double_fork_right_simple_lower_right.png)
![](images/chars/large_flat_top/double_fork_left_simple_lower_left.png)
![](images/chars/large_flat_top/simple_fork_left_double_upper_left.png)
![](images/chars/large_flat_top/double_fork_left_simple_upper_left.png)
![](images/chars/large_flat_top/simple_fork_left_double_right.png)
![](images/chars/large_flat_top/double_fork_left_simple_right.png)
![](images/chars/large_flat_top/simple_fork_left_double_lower_left.png)

![](./images/examples/large_flat_top_mixed.png)

### Construction

If we ignore the line style, this character set can be composed in 11 shapes:

- 1 horizontal bar;
- 6 corners;
- 2 forks used to connect hexagons;
- 2 diagonal bars used to extend the hexagons in order to get bigger ones.

The following image explains how these shapes are built:

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

![](images/construction/large_pointy_top.png)

The vertical bar is supposed to be similar to `┃` (`\u2503`: Box Drawings Heavy Vertical)

#### Double

*Coming soon*

## Small flat-top hexagons

*Coming soon*

## Small pointy-top hexagons

*Coming soon*
