import numpy as np
import logging
import week5
import greeter_lib

def main():
    # Using Python's built-in logging.
    # See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

    # Configure the logger: The options on the first line matter most.
    #   The second line clear the log-file everytime the program runs.
    #   The last two lines add a time-stamp in a format I like.
    logging.basicConfig(filename='week5-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    # logging.warning('And this, too')

    logging.info('Program begins!')

    greeter_lib.greeter("Our program begins!")
    
    logging.info('Beginning first matrix operations!')
    m1 = np.array([[1, 5, 8], [2, 7, 6], [3, 4, 9]])
    week5.wahoovian(m1)
    print("--------------------------------------")
    logging.info('Beginning second matrix operation!')
    m2 = np.array([[-5, 8, 2], [6, -9, -7], [4, 6, 5]])
    week5.wahoovian(m2)
    logging.info('Program ends!')

if __name__ == '__main__':
    main()
