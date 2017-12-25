import sys
import time

import settings as s
import state_transitions as st

from random import randint
from transitions import Machine

from utils import parse_args

logger = s.logger


class LiftStateMachine(object):
    """
        Lift State Machine class which allows you to
          control the lift simulation.
    """
    def __init__(self, floor_num, floor_height, lift_speed, door_time):

        self.floor_num = floor_num
        self.floor_height = floor_height
        self.lift_speed = lift_speed
        self.door_time = door_time
        self.current_lift_pos = None
        self.current_passenger_pos = 0
        self.current_dest_floor = 1
        self.lsm = None
        self.lift_move_time = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=st.lift_states, send_event=True,
                               transitions=st.lift_transitions, initial='init_lift_position')

    def init_start_lift_position(self, event_data):
        """
        This method initialise the first lift position.
          The lift position randomly choose between
          'MIN_FLOOR_NUM' and input 'floor_num'

        :return: None
        """
        if self.current_lift_pos is None:
            self.current_lift_pos = randint(s.MIN_FLOOR_NUM, self.floor_num)
        logger.debug(f'Lift is on the {self.current_lift_pos} floor')

    def wait_while_lift_come(self, event_data):
        """
        This method shows the movement of the lift.

        :param dict event_data: object with current state data

        :return: None
        """
        lift_direction = event_data.kwargs.get('lift_direction', True)
        if lift_direction:
            floors = range(self.current_lift_pos, self.current_passenger_pos + 1)
        else:
            floors = range(self.current_lift_pos, self.current_passenger_pos - 1, -1)

        for floor in floors:
            time.sleep(self.lift_move_time)
            self.current_lift_pos = floor
            logger.debug(f'Current lift position: {floor} floor')

    def open_lift_door(self, event_data):
        """
        This method waiting while lift door is opening.

        :return: None
        """
        time.sleep(self.door_time)
        logger.debug('The door is open. Come in...')

    def start_lift(self, lsm):
        """
        This method trigger lift to the first state.

        :return: None
        """
        self.lsm = lsm
        self.lsm.trigger(st.INIT_LIFT_POSITION_TRIGGER)
        self.lift_move_time = self.calculate_floor_print_time()
        while True:
            self.input_passenger_floor_position()
            self.lsm.trigger(st.GET_LIFT_TRIGGER, lift_direction=self.input_call_lift_command())
            self.lsm.trigger(st.OPEN_LIFT_DOOR_TRIGGER)
            self.current_dest_floor = self.input_destination_floor()

    def stop_lift(self):
        """
        This method is for safe lift stop

        :return: None
        """
        logger.debug(f'\nSTOPPING LIFT... Lift state: {self.lsm.state}, '
                     f'current floor: {self.current_lift_pos}')

    def calculate_floor_print_time(self):
        """
        This method calculate time which shows how long
          lift going from one floor to another

        :return float lift_time: time in second
        """
        return float(self.floor_height / self.lift_speed)

    def input_passenger_floor_position(self):
        """
        This method validate input current passenger position
          and validate input data

        :return: None
        """
        wrong_num, input_passenger_pos = True, -1
        while wrong_num:
            try:
                input_passenger_pos = int(input(f'On which floor are you now? '
                                                f'Input number from 1 to {self.floor_num}: '))
                wrong_num = \
                    True if input_passenger_pos <= 0 or input_passenger_pos > self.floor_num else False
            except ValueError:
                pass
            if wrong_num:
                logger.debug(f'Wrong input data. Floor number should be:'
                             f' 0 < {input_passenger_pos} <= {self.floor_num}')
            else:
                self.current_passenger_pos = input_passenger_pos
                break

    def input_destination_floor(self):
        """
        This method allow to input destination floor number
          and validate input data

        :return input_floor_num: destination floor number
        :rtype: int
        """
        wrong_num, input_floor_num = True, -1
        while wrong_num:
            try:
                input_floor_num = int(input(f'CHOOSE DESTINATION FLOOR. '
                                            f'Input number from 1 to {self.floor_num}: '))
                wrong_num = \
                    True if input_floor_num <= 0 or input_floor_num > self.floor_num else False
            except ValueError:
                pass
            if wrong_num:
                logger.debug(f'Wrong input data. Floor number should be:'
                             f' 0 < {input_floor_num} <= {self.floor_num}')

        return input_floor_num

    def input_call_lift_command(self):
        """
        This method allow to input 'START' command
          and validate input data

        :return: lift direction - if lift is upper than you - True, else - False
        :rtype: bool
        """
        wrong_num, input_cmd = True, ""
        while wrong_num:
            input_cmd = input("For call the lift input 'start': ")
            if input_cmd.lower() == 'start':
                return False if self.current_passenger_pos < self.current_lift_pos else True
            else:
                logger.debug(f'Wrong input data. Input command should be: "start" OR "START"')


def main():
    """
    This method is the main entry point of program

    :return: None
    """
    try:
        args = parse_args()
        if args is None:
            sys.exit()
        lsm = LiftStateMachine(
            floor_num=args.floor_num, floor_height=args.floor_height,
            lift_speed=args.lift_speed, door_time=args.door_time)
        lsm.start_lift(lsm)
    except KeyboardInterrupt:
        lsm.stop_lift()


if __name__ == '__main__':
    main()
