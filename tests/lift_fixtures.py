# -*- coding: utf-8 -*-
import pytest

from collections import namedtuple

from run_lift import LiftStateMachine

import utils_for_tests as uft
import state_transitions as st


@pytest.fixture
def lift_state_machine(request):
    floor_num, floor_height, lift_speed, door_time = (10, 2, 2, 1)
    lsm = LiftStateMachine(
            floor_num=floor_num, floor_height=floor_height,
            lift_speed=lift_speed, door_time=door_time
    )
    _test_res = namedtuple('TestRes', ['floor_num', 'floor_height',
                                       'lift_speed', 'door_time', 'lsm'])
    return _test_res(floor_num, floor_height, lift_speed, door_time, lsm)


@pytest.fixture(params=[(10, 2, 2, 1), (10, 3, 3, 1)], ids=uft.idf_lst_params)
def init_lift_state_machine(request):
    floor_num, floor_height, lift_speed, door_time = request.param
    lsm = LiftStateMachine(
            floor_num=floor_num, floor_height=floor_height,
            lift_speed=lift_speed, door_time=door_time
    )
    _test_res = namedtuple('TestRes', ['floor_num', 'floor_height',
                                       'lift_speed', 'door_time', 'lsm'])
    return _test_res(floor_num, floor_height, lift_speed, door_time, lsm)


@pytest.fixture(params=[(st.OPEN_LIFT_DOOR_TRIGGER, 'open_lift_door'),
                        (st.INIT_LIFT_POSITION_TRIGGER, 'init_lift_position')],
                ids=uft.idf_lst_trigger_pos)
def trigger_lsm_state_pos(request):
    trigger, state = request.param
    _test_res = namedtuple('TestRes', ['trigger', 'state'])
    return _test_res(trigger, state)

