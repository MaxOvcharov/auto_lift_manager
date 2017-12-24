from utils import parse_args
from settings import logger


def main():
    """
    This methot is the main entry point of program

    :return: None
    """
    args = parse_args()
    logger.debug(f'Show params: {args}')


if __name__ == '__main__':
    main()
