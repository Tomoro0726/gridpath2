
def grid(x1, y1, x2, y2):
    """Calculate grid path and intersection points between two coordinates.

    Args:
        x1, y1: Starting point coordinates
        x2, y2: Ending point coordinates

    Returns:
        dict: Dictionary containing:
            - "grid": List of grid points [[x1, y1], [x2, y2], ...]
            - "intersect": List of intersection points [[x1, y1], [x2, y2], ...]
    """

    # グリッドポイントとパスの初期化
    x1_grid, y1_grid = int(x1), int(y1)
    x2_grid, y2_grid = int(x2), int(y2)
    grid_list = [[x1_grid, y1_grid]]
    intersect_point = [[x1, y1]]
    

    # 同一点の場合は早期リターン
    if x1_grid == x2_grid and y1_grid == y2_grid:
        intersect_point.append([x2, y2])
        return {"grid": grid_list, "intersect": intersect_point, }

    # 水平線の処理
    if y1 == y2:
        direction = 1 if x2 > x1 else -1
        for i in range(abs(x2_grid - x1_grid)):
            prev = grid_list[-1]
            next_point = [prev[0] + direction, prev[1]]
            grid_list.append(next_point)
            intersect_point.append([next_point[0], y1])
        intersect_point.append([x2, y2])
        return {"grid": grid_list, "intersect": intersect_point, }

    # 垂直線の処理
    if x1 == x2:
        direction = 1 if y2 > y1 else -1
        for i in range(abs(y2_grid - y1_grid)):
            prev = grid_list[-1]
            next_point = [prev[0], prev[1] + direction]
            grid_list.append(next_point)
            intersect_point.append([x1, next_point[1]])
        intersect_point.append([x2, y2])
        return {"grid": grid_list, "intersect": intersect_point, }

    # 傾きの計算
    dydx = (y2 - y1) / (x2 - x1)

    # 傾きが1または-1の対角線の処理
    if abs(dydx) == 1:
        x_direction = 1 if x2 > x1 else -1
        y_direction = 1 if y2 > y1 else -1
        for i in range(abs(x2_grid - x1_grid)):
            prev = grid_list[-1]
            next_point = [prev[0] + x_direction, prev[1] + y_direction]
            grid_list.append(next_point)
            intersect_point.append(
                [x1_grid+x_direction*(i+1), y1_grid+y_direction*(i+1)])
        if dydx == -1:
            for point in grid_list:
                point[1] -= 1
        intersect_point[-1] = [x2, y2]
        return {"grid": grid_list, "intersect": intersect_point, }

    # 一般的なケースの処理
    iteration_count = 0

    while True:
        current = grid_list[-1]
        
        #終了条件
        if current[0] == x2_grid and current[1] == y2_grid:
            return {"grid": grid_list, "intersect": intersect_point, }
        if (current == [x2_grid-1, y2_grid -1] or
            current == [x2_grid, y2_grid - 1] or
            current == [x2_grid - 1, y2_grid]):
            return {"grid": grid_list, "intersect": intersect_point, }

        # 傾きの方向と位置に基づいて次のポイントを計算
        if dydx > 0:
            if x2 > x1:  # 正の傾きで右に移動
                next_x_intersect = (current[1] + 1 - y1) / dydx + x1
                if current[0] <= next_x_intersect < current[0] + 1:
                    next_point = [current[0], current[1] + 1]
                    next_intersect = [next_x_intersect, current[1]+1]
                else:
                    next_point = [current[0] + 1, current[1]]
                    next_intersect = [current[0]+1, dydx*(current[0]+1-x1)+y1]
            else:  # 正の傾きで左に移動
                next_x_intersect = (current[1] - y1) / dydx + x1
                if current[0] <= next_x_intersect < current[0] + 1:
                    next_point = [current[0], current[1] - 1]
                    next_intersect = [next_x_intersect, current[1]]
                else:
                    next_point = [current[0] - 1, current[1]]
                    next_intersect = [current[0], dydx*(current[0]-x1)+y1]
        else:  # 負の傾き
            if x2 > x1:  # 負の傾きで右に移動
                next_x_intersect = (current[1] - y1) / dydx + x1
                if current[0] <= next_x_intersect < current[0] + 1:
                    next_point = [current[0], current[1] - 1]
                    next_intersect = [next_x_intersect, current[1]]
                else:
                    next_point = [current[0] + 1, current[1]]
                    next_intersect = [current[0]+1, dydx*(current[0]+1-x1)+y1]
            else:  # 負の傾きで左に移動
                next_x_intersect = (current[1] + 1 - y1) / dydx + x1
                if current[0] <= next_x_intersect <= current[0] + 1:
                    next_point = [current[0], current[1] + 1]
                    next_intersect = [next_x_intersect, current[1]+1]
                else:
                    next_point = [current[0] - 1, current[1]]
                    next_intersect = [current[0], dydx*(current[0]-x1)+y1]
        intersect_point.append(next_intersect)
        grid_list.append(next_point)