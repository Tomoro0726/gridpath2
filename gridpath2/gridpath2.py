def grid(x1: float, y1: float, x2: float, y2: float) -> dict:
    """2点間のグリッドパスと交点を計算する関数

    Args:
        x1, y1: 開始点の座標
        x2, y2: 終了点の座標

    Returns:
        dict: {
            "grid": グリッドポイントのリスト [[x, y], ...],
            "intersect": 交点のリスト [[x, y], ...],
            "timeout": タイムアウト状態 (bool)
        }
    """
    MAX_ITERATIONS = 1000

    # グリッドポイントの初期化
    # グリッドポイントとパスの初期化
    x1_grid = int(x1) if x1 >= 0 else int(x1) - (1 if x1 != int(x1) else 0)
    y1_grid = int(y1) if y1 >= 0 else int(y1) - (1 if y1 != int(y1) else 0)
    x2_grid = int(x2) if x2 >= 0 else int(x2) - (1 if x2 != int(x2) else 0)
    y2_grid = int(y2) if y2 >= 0 else int(y2) - (1 if y2 != int(y2) else 0)
    grid_list = [[x1_grid, y1_grid]]
    intersect_points = [[x1, y1]]

    # 同一点の場合
    if x1_grid == x2_grid and y1_grid == y2_grid:
        intersect_points.append([x2, y2])
        return {"grid": grid_list, "intersect": intersect_points, "timeout": False}

    # 傾きの計算
    dx = x2 - x1
    dy = y2 - y1
    slope = dy / dx if dx != 0 else float('inf')

    # 水平線の場合
    if dy == 0:
        direction = 1 if x2 > x1 else -1
        for _ in range(abs(x2_grid - x1_grid)):
            next_x = grid_list[-1][0] + direction
            grid_list.append([next_x, y1_grid])
            intersect_points.append([next_x, y1])
        intersect_points.append([x2, y2])
        return {"grid": grid_list, "intersect": intersect_points, "timeout": False}

    # 垂直線の場合
    if dx == 0:
        direction = 1 if y2 > y1 else -1
        for _ in range(abs(y2_grid - y1_grid)):
            next_y = grid_list[-1][1] + direction
            grid_list.append([x1_grid, next_y])
            intersect_points.append([x1, next_y])
        intersect_points.append([x2, y2])
        return {"grid": grid_list, "intersect": intersect_points, "timeout": False}

    # 45度の対角線の場合
    if abs(slope) == 1:
        x_direction = 1 if x2 > x1 else -1
        y_direction = 1 if y2 > y1 else -1
        for i in range(abs(x2_grid - x1_grid)):
            current = grid_list[-1]
            grid_list.append([current[0] + x_direction, current[1] + y_direction])
            intersect_points.append([
                x1_grid + x_direction * (i + 1),
                y1_grid + y_direction * (i + 1)
            ])
        if slope == -1:
            for point in grid_list:
                point[1] -= 1
        intersect_points[-1] = [x2, y2]
        return {"grid": grid_list, "intersect": intersect_points, "timeout": False}

    # 一般的なケースの処理
    moving_right = x2 > x1
    
    #終了グリッドの列挙
    end_x= [x2_grid]
    end_y= [y2_grid]
    
    if x2==x2_grid:
        end_x.append(x2_grid-1)
    if y2==y2_grid:
        end_y.append(y2_grid-1)
    
    for iteration in range(MAX_ITERATIONS):
        current = grid_list[-1]
        
        # 終了条件
        if current[0] in end_x and current[1] in end_y:
            intersect_points.append([x2, y2])
            return {"grid": grid_list, "intersect": intersect_points, "timeout": False}
        

        # 次の交点とグリッドポイントの計算
        if slope > 0:
            if moving_right:
                next_x_intersect = (current[1] + 1 - y1) / slope + x1
                if current[0] <= next_x_intersect < current[0] + 1:
                    next_point = [current[0], current[1] + 1]
                    next_intersect = [next_x_intersect, current[1] + 1]
                else:
                    next_point = [current[0] + 1, current[1]]
                    next_intersect = [current[0] + 1, slope * (current[0] + 1 - x1) + y1]
            else:
                next_x_intersect = (current[1] - y1) / slope + x1
                if current[0] <= next_x_intersect < current[0] + 1:
                    next_point = [current[0], current[1] - 1]
                    next_intersect = [next_x_intersect, current[1]]
                else:
                    next_point = [current[0] - 1, current[1]]
                    next_intersect = [current[0], slope * (current[0] - x1) + y1]
        else:
            if moving_right:
                next_x_intersect = (current[1] - y1) / slope + x1
                if current[0] <= next_x_intersect < current[0] + 1:
                    next_point = [current[0], current[1] - 1]
                    next_intersect = [next_x_intersect, current[1]]
                else:
                    next_point = [current[0] + 1, current[1]]
                    next_intersect = [current[0] + 1, slope * (current[0] + 1 - x1) + y1]
            else:
                next_x_intersect = (current[1] + 1 - y1) / slope + x1
                if current[0] <= next_x_intersect <= current[0] + 1:
                    next_point = [current[0], current[1] + 1]
                    next_intersect = [next_x_intersect, current[1] + 1]
                else:
                    next_point = [current[0] - 1, current[1]]
                    next_intersect = [current[0], slope * (current[0] - x1) + y1]

        intersect_points.append(next_intersect)
        grid_list.append(next_point)

    # タイムアウトの場合
    print("Timeout")
    return {"grid": grid_list, "intersect": intersect_points, "timeout": True}