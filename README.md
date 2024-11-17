# gridpath2

GridPath is a Python library for calculating grid-based paths and intersection points between two coordinates. It's particularly useful for applications requiring precise path tracking on a grid system, such as robotics, game development, or computer graphics.

## Features

- Calculate grid-aligned paths between any two points
- Determine exact intersection points with grid lines
- Support for horizontal, vertical, and diagonal paths
- Handle special cases like same-point paths and 45-degree angles
- Return both grid points and precise intersection coordinates

## Installation

```bash
pip install gridpath2
```

## Usage

Basic usage example:

```python
from gridpath2 import grid

# Calculate path between two points
result = grid(x1=1.5, y1=2.3, x2=4.7, y2=6.8)

# Access the results
grid_points = result["grid"]      # List of grid points traversed
intersections = result["intersect"] # List of exact intersection points
```

The function returns a dictionary containing:

- `grid`: List of grid points the path traverses through
- `intersect`: List of exact coordinates where the path intersects with grid lines

### Example Scenarios

1. Horizontal path:

```python
path = grid(1.5, 2.0, 4.5, 2.0)
# Returns path along y=2
```

2. Vertical path:

```python
path = grid(2.0, 1.5, 2.0, 4.5)
# Returns path along x=2
```

3. Diagonal path (45 degrees):

```python
path = grid(1.0, 1.0, 3.0, 3.0)
# Returns diagonal path with slope=1
```

4. General case:

```python
path = grid(1.5, 2.3, 4.7, 6.8)
# Returns optimal grid path with precise intersections
```

## Function Details

```python
def grid(x1: float, y1: float, x2: float, y2: float) -> dict:
    """Calculate grid path and intersection points between two coordinates.

    Args:
        x1, y1: Starting point coordinates
        x2, y2: Ending point coordinates

    Returns:
        dict: Dictionary containing:
            - "grid": List of grid points [[x1, y1], [x2, y2], ...]
            - "intersect": List of intersection points [[x1, y1], [x2, y2], ...]
    """
```

## Technical Details

The library handles several special cases:

- Same point paths
- Horizontal lines
- Vertical lines
- 45-degree diagonal lines
- General cases with arbitrary slopes

For general cases, the algorithm:

1. Calculates the slope between points
2. Determines the next grid intersection based on slope direction
3. Tracks both grid points and exact intersections
4. Handles positive and negative slopes differently
5. Provides precise intersection coordinates

## Use Cases

- Robot path planning
- Game development (grid-based movement)
- Computer graphics (line rasterization)
- Scientific visualization
- CAD applications

## Requirements

- Python 3.6+

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
