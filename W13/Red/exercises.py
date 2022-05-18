"""Breth traversal (DTH) points I can reach
Depth
Diskstase"""

from graph import Graph

class Graph2(Graph):

    def checkPath(self, start, end):
        """Check if there is a path from start to end in the graph"""
        if start == end:
            return True
        if start not in self._vertices:
            return False
        for v in self._vertices[start]:
            if self.checkPath(v, end):
                return True
        return False

    def countNotReachable(self):
        """Count the number of vertices that are not reachable from the root"""
        count = 0
        for v in self._vertices:
            if not self.checkPath(self._root, v):
                count += 1
        return count