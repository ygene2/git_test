# -*- coding: utf-8 -*-

import time


def main():

    st = time.time()
    for i in range(10):
        print(i)

    et = time.time()
    print('time elapsed: {} sec'.format(et - st))


if __name__ == '__main__':

    main()
