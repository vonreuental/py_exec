def fight(robot_1, robot_2, tactics):
    # Determine the fastest robot for the rest of the fight
    def p_result(name):
        return f"{name['name']} has won the fight."

    if robot_2['speed'] > robot_1['speed']:
        robot_first = robot_2
        robot_second = robot_1
    else:
        robot_first = robot_1
        robot_second = robot_2

    while (len(robot_first['tactics']) > 0) or (len(robot_second['tactics']) > 0):
        if len(robot_first['tactics']) > 0:
            robot_second['health'] -= tactics[robot_first['tactics'].pop(0)]
        if robot_second['health'] <= 0:
            return p_result(robot_first)
        if len(robot_second['tactics']) > 0:
            robot_first['health'] -= tactics[robot_second['tactics'].pop(0)]
        if robot_first['health'] <= 0:
            return p_result(robot_second)
    else:
        if robot_first['health'] == robot_second['health']:
            return "The fight was a draw."
        else:
            winner = robot_first['name'] if robot_first['health'] > robot_second['health'] else robot_second['name']
            return p_result(winner)


robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
print(fight(robot_1, robot_2, tactics))
