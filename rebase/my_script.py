# -*- coding: utf-8 -*-

import time


def main():

    start_time = time.time()
    for i in range(10):
        print(i)

    end_time = time.time()
    print('time elapsed: {} sec'.format(end_time - start_time))


if __name__ == '__main__':

    main()
