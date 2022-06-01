class WaterJug:
    def __init__(self, jug_capacity, goal_state):
        self.jug_capacity=jug_capacity
        self.goal_state=goal_state

    def is_goal_state(self, state):
        return state == self.goal_state

    def dfs(self):
        solutions = []
        def _dfs(path, seen):
            if (self.is_goal_state(path[-1])):
                solutions.append(path)
                return
            
            def proceed(ns):
                if ns not in seen:
                    seen.add(ns)
                    _dfs(path + [ns], seen.copy())
            

            cur_state = path[-1]

            #fill left jug
            new_state = (self.jug_capacity[0], cur_state[1])
            proceed(new_state)

            #fill right jug
            new_state = (cur_state[0], self.jug_capacity[1])
            proceed(new_state)

            #empty left jug
            new_state = (0, cur_state[1])
            proceed(new_state)

            #empty right jug
            new_state = (cur_state[0],0)
            proceed(new_state)


            #transfer left jug to right jug 
            rc = self.jug_capacity[1] - cur_state[1]
            if rc >= cur_state[0]:
                new_state = (0,cur_state[1] + cur_state[0])
            else:
                new_state = (cur_state[0] - rc, self.jug_capacity[1])
            proceed(new_state)


            #transfer right jug to left jug
            lc = self.jug_capacity[0] - cur_state[0]
            if lc >= cur_state[1]:
                new_state = (cur_state[0] + cur_state[1], 0)
            else:
                new_state = (self.jug_capacity[0], cur_state[1] - lc)
            proceed(new_state)

        _dfs([(0,0)],set([(0,0)]))
        return solutions

def main():
    wj = WaterJug((4, 3), (2, 0))
    solns = wj.dfs()
    for soln in solns:
        print(soln)

main()