class AOStar:
    """ Class to run the AO* algorithm.
    """
    
    def _init_(self, po_problem, heuristic):
        """
        Parameters
        ----------
        po_problem : poProblem
            The partially observable problem to be solved. 
        heuristic : function
            The heuristic function to guide the search.
        """
        self.po_problem = po_problem
        self.heuristic = heuristic
        
    def solve(self):
        start_state=  self.po_problem.getInitialState()
        start_node = Node(self.po_problem, start_state, None, None)
        i = 0
        node = {}
        frontier = {}
        path = []
        node[i] = start_node
        frontier[i] = start_node.pathCost + self.heuristic(start_node.state)

        while True :
            min_node_id = min(frontier, key=frontier.get)
            current_node = node[min_node_id]

            if self.po_problem.isFinal(current_node.state):
                path = []
                while current_node is not None:
                    if current_node.actionFromFather is not None:  # Éviter d'ajouter None pour le nœud de départ
                        path.append(current_node.actionFromFather)
                    current_node = current_node.fatherNode
                path.reverse()
                return path

            del frontier[min_node_id]

            for action in self.po_problem.actions(current_node.state):
                child_states = self.po_problem.update(current_node.state, action)
                for child_state in child_states:
                    child_node = Node(self.po_problem, child_state, current_node, action)
                    i = i+1
                    node[i] = child_node
                    frontier[i] = child_node.pathCost + self.heuristic(child_node.state)




    def solve(self):
        """
        Applies the and or search algorithm
        -------
        Returns 
        A contingency plan
        """
        plan = self.orSearch(self.po_problem.getInitialState(), [])
        if plan is None:
            print("Failure")
        else:
            print(plan)

    def orSearch(self, b_state, path):
        """
        Returns list of actions, conditional plan
        Parameters
        ----------
        b_State : set
            A beliefState, i.e., a set of states.
        path : list
            A list of belief states leading to the goal state
        Returns
        -------
        list
            list of actions, conditional plan
        """
        pass
        print("")
        print("")
        print("-----Belief state----")
        self.po_problem.printBeliefStates(b_state)
        #the conditional plan
        plan = []
        #Check if any state of the belief state is a goal state 
        if self.po_problem.isFinal(b_state):
            return plan
        #Check if the belief state is on path
        if b_state in path : 
            return None
        for action in self.po_problem.actions(b_state):
            #add the current belief state to the path
            path.append(b_state)
            #update the list of new belief states 
            next_possible_states = self.po_problem.update(b_state,action)

            print("Action :", action)
            # print path
            print("-------- Path   :")
            for b_st in path:
                self.po_problem.printBeliefStates(b_st)
            print("-------- Next Possible States  :")
            #run every belief state in the set of next possible states
            for states in next_possible_states:
                self.po_problem.printBeliefStates(states)
                plan_i = self.andSearch(states,path)
                if plan_i is not None :
                    plan+= plan_i
            if plan is not None:
                plan = [(b_state,action)]+plan
        return plan


    def andSearch(self, b_states, path):
        """
        TODO
        Returns list of actions, conditional plan
        Parameters
        ----------
        b_State : set
            A beliefState, i.e., a set of states.
        path : list
            A list of belief states 
        Returns
        -------
        list
            list of actions, conditional plan 
        """
        pass
        #initiate the conditional plan
        plan = []
        plan = self.orSearch(b_states,path)
        if plan is None:
            return None
        return plan

