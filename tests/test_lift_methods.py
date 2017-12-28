import pytest
import transitions

import utils_for_tests as uft
import state_transitions as st


@pytest.mark.critical_test
def test_lsm_calculate_floor_print_time_positive(init_lift_state_machine):
    in_param = init_lift_state_machine
    res = in_param.lsm.calculate_floor_print_time()
    assert res == float(in_param.floor_height / in_param.lift_speed)


@pytest.mark.critical_test
def test_lsm_states_positive(init_lift_state_machine, trigger_lsm_state_pos):
    in_param1 = init_lift_state_machine
    in_param2 = trigger_lsm_state_pos

    in_param1.lsm.trigger(in_param2.trigger)
    res = in_param1.lsm.state
    assert res == in_param2.state


@pytest.mark.critical_test
@pytest.mark.parametrize("trigger", [st.GO_TO_CHOSEN_FLOOR_TRIGGER, st.CLOSE_LIFT_DOOR_TRIGGER],
                         ids=uft.idf_lst_trigger_neg)
def test_lsm_states_negative(lift_state_machine, trigger):
    in_param1 = lift_state_machine
    with pytest.raises(transitions.core.MachineError):
        in_param1.lsm.trigger(trigger)

