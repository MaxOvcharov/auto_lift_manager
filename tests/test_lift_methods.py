import pytest


@pytest.mark.critical_test
def test_lsm_calculate_floor_print_time_positive(init_lift_state_machine):
    in_param = init_lift_state_machine
    res = in_param.lsm.calculate_floor_print_time()
    assert res == float(in_param.floor_height / in_param.lift_speed)


@pytest.mark.critical_test
def test_lsm_states_positive(init_lift_state_machine, trigger_lsm_state):
    in_param1 = init_lift_state_machine
    in_param2 = trigger_lsm_state

    in_param1.lsm.trigger(in_param2.trigger)
    res = in_param1.lsm.state
    assert res == in_param2.state
