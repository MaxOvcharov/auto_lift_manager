def idf_lst_params(val):
    return f"Floor_num: {val[0]}, Floor_height: {val[1]}, " \
           f"Lift_speed: {val[2]}, Door_time: {val[3]}"


def idf_lst_trigger_pos(val):
    return f"TRIGGER NAME: {val[0]}, STATE: {val[1]}"


def idf_lst_trigger_neg(val):
    return f"TRIGGER NAME: {val}"
