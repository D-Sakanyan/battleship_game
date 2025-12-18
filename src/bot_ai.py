import random

BOARD_SIZE = 10

class BotAI:
    def __init__(self):
        self.mode = "random"
        self.hits = []
        self.axis = None
        self.queue = []
        self.shots = set()

    def next_move(self):
        if self.mode == "random":
            return self.random_shot()
        elif self.mode == "target":
            return self.target_shot()
        elif self.mode == "axis":
            return self.axis_shot()

    def random_shot(self):
        while True:
            r = random.randint(0, BOARD_SIZE-1)
            c = random.randint(0, BOARD_SIZE-1)
            if (r,c) not in self.shots:
                self.shots.add((r,c))
                return (r,c)

    def target_shot(self):
        while self.queue:
            r,c = self.queue.pop(0)
            if (r,c) not in self.shots and 0<=r<BOARD_SIZE and 0<=c<BOARD_SIZE:
                self.shots.add((r,c))
                return (r,c)

        self.mode = "random"
        return self.random_shot()

    def axis_shot(self):
        r1,c1 = self.hits[0]
        r2,c2 = self.hits[1]
        dr = 0
        dc = 0
        if self.axis == "H":
            dc = 1
        else:
            dr = 1

        for sign in [1,-1]:
            for i in range(1, BOARD_SIZE):
                nr = r1 + dr*i*sign
                nc = c1 + dc*i*sign
                if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                    if (nr,nc) not in self.shots:
                        self.shots.add((nr,nc))
                        return (nr,nc)

        self.mode = "random"
        self.hits.clear()
        self.axis = None
        return self.random_shot()

    def process_result(self, coord, result):
        if result.startswith("hit"):
            if result.endswith("destroyed"):
                self.mode = "random"
                self.hits.clear()
                self.axis = None
                self.queue.clear()
            else:
                if not self.hits:
                    self.hits.append(coord)
                    self.mode = "target"
                    r,c = coord
                    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr,nc = r+dr,c+dc
                        if 0<=nr<BOARD_SIZE and 0<=nc<BOARD_SIZE and (nr,nc) not in self.shots:
                            self.queue.append((nr,nc))
                elif len(self.hits)==1:
                    r0,c0 = self.hits[0]
                    r1,c1 = coord
                    if r0==r1:
                        self.axis="H"
                    else:
                        self.axis="V"
                    self.hits.append(coord)
                    self.mode="axis"
                else:
                    self.hits.append(coord)
        else:
            pass
