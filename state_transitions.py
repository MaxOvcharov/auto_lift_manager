
INIT_LIFT_POSITION_TRIGGER = 'INIT_LIFT_POSITION'
GET_LIFT_TRIGGER = 'GET_LIFT'
OPEN_LIFT_DOOR_TRIGGER = 'OPEN_LIFT_DOOR'
CLOSE_LIFT_DOOR_TRIGGER = 'CLOSE_LIFT_DOOR'
CHOOSE_FLOOR_NUM_TRIGGER = 'CHOOSE_FLOOR_NUM'
GO_TO_CHOSEN_FLOOR_TRIGGER = 'GO_TO_CHOSEN_FLOOR'

lift_states = [
    'init_lift_position', 'get_lift', 'open_lift_door', 'close_lift_door',
    'choose_floor_num', 'go_to_chosen_floor'
]

lift_transitions = [
    {
        'trigger': INIT_LIFT_POSITION_TRIGGER,
        'source': '*',
        'dest': 'init_lift_position',
        'after': 'init_start_lift_position'
    },
    {
        'trigger': GET_LIFT_TRIGGER,
        'source': 'init_lift_position',
        'dest': 'get_lift',
        'after': 'wait_while_lift_come'
    },
    {
        'trigger': OPEN_LIFT_DOOR_TRIGGER,
        'source': 'get_lift',
        'dest': 'open_lift_door',
        'after': 'open_lift_door'
    },
    {
        'trigger': CLOSE_LIFT_DOOR_TRIGGER,
        'source': 'open_lift_door',
        'dest': 'close_lift_door',
        'after': 'close_lift_door'
    },
    {
        'trigger': CHOOSE_FLOOR_NUM_TRIGGER,
        'source': 'close_lift_door',
        'dest': 'choose_floor_num',
        'after': 'check_chosen_flow_num'
    },
    {
        'trigger': GO_TO_CHOSEN_FLOOR_TRIGGER,
        'source': 'choose_floor_num',
        'dest': 'go_to_selected_floor',
        'after': 'go_to_chosen_floor'
    },
    {
        'trigger': OPEN_LIFT_DOOR_TRIGGER,
        'source': 'go_to_chosen_floor',
        'dest': 'open_lift_door',
        'after': 'open_door_and_wait'
    },

]
