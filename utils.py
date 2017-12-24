import argparse

from settings import DEFAULT_FLOW_NUM, DEFAULT_FLOW_HEIGHT, \
    DEFAULT_LIFT_SPEED, DEFAULT_DOOR_TIME


def parse_args():
    """
        This method parse input params from command line.
        Example:
        run_lift.py --flow_num 9 --flow_height 2 --lift_speed 2 --door_time 3

        :return: args with attributes - args.
        :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description='Simple automated lift simulator. '
                                                 'Input following params')
    parser.add_argument('-n', '--flow_num', type=float, nargs='?',
                        default=DEFAULT_FLOW_NUM,
                        help=f'Number of flow (5 <= n <= 20). Default - {DEFAULT_FLOW_NUM}')
    parser.add_argument('-f', '--flow_height', type=float, nargs='?',
                        default=DEFAULT_FLOW_HEIGHT,
                        help=f'Height of one flow(meter). Default - {DEFAULT_FLOW_HEIGHT}')
    parser.add_argument('-s', '--lift_speed', type=float, nargs='?',
                        default=DEFAULT_LIFT_SPEED,
                        help=f'Speed of the lift(meter per second). '
                             f'Default - {DEFAULT_LIFT_SPEED}')
    parser.add_argument('-t', '--door_time', type=float, nargs='?',
                        default=DEFAULT_DOOR_TIME,
                        help=f'time of door opening/closing (second). '
                             f'Default - {DEFAULT_DOOR_TIME}')

    return parser.parse_args()

