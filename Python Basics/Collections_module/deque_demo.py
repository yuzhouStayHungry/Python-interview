# -*- coding: utf-8 -*-
# @Time      : 2020-04-24 00:06
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : deque_demo.py
# @Software  : PyCharm

# -*- coding: utf-8 -*-
"""
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
"""
import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print('\r%s' % ''.join(fancy_loading))
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)

# Result:

# 一个无尽循环的跑马灯
# ------------->-------
