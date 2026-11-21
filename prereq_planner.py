"""
Homework 6: The Prerequisite Planner -- starter.

Complete has_cycle and topological_sort below. See
Homework 6 The Prerequisite Planner.md, Part B, for the full requirements.
"""

from typing import Dict, List, Optional


def has_cycle(graph: Dict[str, List[str]]) -> bool:
    """
    Recursive DFS. Track both a permanent "visited" set and a
    temporary "on the current recursion path" set to detect back
    edges (Part A, Question 4). Must work across disconnected
    components.
    """
    visited = set()
    on_path = set()

    def dfs(course):
        if course in on_path:
            return True

        if course is visited:
            return False

        visited.add(course)
        on_path.add(course)

        for neighbor in graph.get(course, []):
            if dfs(neighbor):
                return True

        on_path.remove(course)
        return False

    for course in graph:
        if dfs(course):
            return True

    return False


def topological_sort(graph: Dict[str, List[str]]) -> Optional[List[str]]:
    """
    Return a valid topological order via DFS finish-time ordering
    (Part A, Questions 2-3), or None if the graph contains a cycle.
    """
    if has_cycle(graph):
        return None

    visited = set()
    finish_order = []

    def dfs(course):
        if course in visited:
            return

        visited.add(course)

        for neighbor in graph.get(course, []):
            dfs(neighbor)

        finish_order.append(course)

    for course in graph:
        dfs(course)

    finish_order.reverse()
    return finish_order
