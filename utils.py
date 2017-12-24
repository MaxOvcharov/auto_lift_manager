import argparse

import settings as s

logger = s.logger


def parse_args():
    """
        This method parse input params from command line.
        Example:
        run_lift.py --floor_num 9 --floor_height 2 --lift_speed 2 --door_time 3

        :return args: args with attributes - args.
        :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description='Simple automated lift simulator. '
                                                 'Input following params')
    parser.add_argument('-n', '--floor_num', type=int, nargs='?',
                        default=s.DEFAULT_FLOOR_NUM,
                        help=f'Number of floors ({s.MIN_FLOOR_NUM} <= n <= {s.MAX_FLOOR_NUM}). '
                             f'Default - {s.DEFAULT_FLOOR_NUM}')
    parser.add_argument('-f', '--floor_height', type=float, nargs='?',
                        default=s.DEFAULT_FLOOR_HEIGHT,
                        help=f'Height of one floor: '
                             f'{s.MIN_FLOOR_HEIGHT} <= f <= {s.MAX_FLOOR_HEIGHT} (meter).'
                             f' Default - {s.DEFAULT_FLOOR_HEIGHT}')
    parser.add_argument('-s', '--lift_speed', type=float, nargs='?',
                        default=s.DEFAULT_LIFT_SPEED,
                        help=f'Speed of the lift:'
                             f'{s.MIN_LIFT_SPEED} <= s <= {s.MAX_LIFT_SPEED} (meter per sec).'
                             f' Default - {s.DEFAULT_LIFT_SPEED}')
    parser.add_argument('-t', '--door_time', type=float, nargs='?',
                        default=s.DEFAULT_DOOR_TIME,
                        help=f'time of door opening/closing:'
                             f'{s.MIN_LIFT_SPEED} <= s <= {s.MAX_LIFT_SPEED} (sec).'
                             f' Default - {s.DEFAULT_DOOR_TIME}')
    args = parser.parse_args()

    wrong_params = False

    if s.MIN_FLOOR_NUM > args.floor_num or args.floor_num > s.MAX_FLOOR_NUM:
        logger.error(f"Floor number should be in range: "
                     f"{s.MIN_FLOOR_NUM} <= n <= {s.MAX_FLOOR_NUM}. "
                     f"Current - {args.floor_num}")
        wrong_params = True

    if s.MIN_FLOOR_HEIGHT > args.floor_height or args.floor_height > s.MAX_FLOOR_HEIGHT:
        logger.error(f"Floor height should be in range: "
                     f"{s.MIN_FLOOR_HEIGHT} <= n <= {s.MAX_FLOOR_HEIGHT}. "
                     f"Current - {args.floor_height}")
        wrong_params = True

    if s.MIN_LIFT_SPEED > args.lift_speed or args.lift_speed > s.MAX_LIFT_SPEED:
        logger.error(f"Lift speed should be in range: "
                     f"{s.MIN_LIFT_SPEED} <= n <= {s.MAX_FLOOR_HEIGHT}. "
                     f"Current - {args.lift_speed}")
        wrong_params = True

    if s.MIN_LIFT_SPEED > args.door_time or args.lift_speed > s.MAX_LIFT_SPEED:
        logger.error(f"Lift speed should be in range: "
                     f"{s.MIN_LIFT_SPEED} <= n <= {s.MAX_FLOOR_HEIGHT}. "
                     f"Current - {args.lift_speed}")
        wrong_params = True

    return args if not wrong_params else None

