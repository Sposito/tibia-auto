class Sequence():


    def __init__(self, seq):
        self._seq_expanded = []
        self.seq = seq
        self.repeat = True
        for act in seq:
            self._seq_expanded.append(act)

            for i in range(act.cooldown_time - 1):
                self._seq_expanded.append(None)
        self.__len__ = len(self._seq_expanded)

    def query(self, i):
        i = i % self.__len__

        return self._seq_expanded[i]