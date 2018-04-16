""" timer.py
Utilitaire pour mesurer le temps.
"""

import time


class Timer:
    """Permet d'assurer les fps voulus."""

    def __init__(self, fps):
        self.__fps = fps
        self.__frame = 0
        self.__start = None

    def tick(self):
        """Attend jusqu'à la prochaine frame."""
        if self.__start is None:
            self.__start = time.perf_counter()
        self.__frame += 1
        target = self.__frame / self.__fps
        passed = time.perf_counter() - self.__start
        differ = target - passed
        if differ < 0:
            # raise ValueError('cannot maintain desired FPS rate')
            return True
        time.sleep(differ)
        return False
