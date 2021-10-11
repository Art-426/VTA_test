class Point:
    # point_check関数　現在の得点（下一桁）を出す
    def point_check(hands):
        sum_point = 0
        for i in hands:
            point = i[-1]
            if point == 'A':
                sum_point += 1
            elif point == 'J' or point == 'Q' or point =='K':
                sum_point += 0
            else:
                sum_point += int(point)
        sum_point = str(sum_point)
        point = int(sum_point[-1])

        return point
    
    def devidend(chip, odds):
        chip *= odds
        return int(chip)


class Natural:
    # natural_check関数　ナチュラルか判定する
    def natural_check(check_point):
        natural_flag = False
        if check_point == 8 or check_point == 9:
            natural_flag = True
        if natural_flag:
            if check_point == 8:
                print('natural_8!')
            elif check_point == 9:
                print('natural_9!')
        else:
            print()
        return natural_flag

# class DrawCheck:
#     def banker_draw():
