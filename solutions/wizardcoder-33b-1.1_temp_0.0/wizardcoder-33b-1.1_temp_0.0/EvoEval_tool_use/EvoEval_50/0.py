from typing import List

def validate_task_input(tasks: List[str]) -> bool:
    """
    takes as input a list of tasks. 
    Returns True if the list is not empty and all elements are strings, else returns False
    """
    if not tasks or not all(isinstance(task, str) for task in tasks):
        return False
    return True

def validate_priority_input(priorities: List[int]) -> bool:
    """
    takes as input a list of priorities. 
    Returns True if the list is not empty and all elements are integers between 1 and 5, else returns False
    """
    if not priorities or not all(isinstance(priority, int) for priority in priorities):
        return False
    if not all(1 <= priority <= 5 for priority in priorities):
        return False
    return True
def create_todo_list(tasks: List[str], priorities: List[int]) -> List[Tuple[str, int]]:
    """
    Takes as input a list of tasks and their corresponding priorities. 
    Returns a list of tasks sorted by their priorities in descending order. 
    If two tasks have the same priority, they should be sorted in the order they were added.
    
    if priority values are not between 1 to 5 inclusive, please return an empty list
    additionally, if the task list is not all strings, also return an empty list
    
    e.g., create_todo_list(['task2', 'task1'], [1, 2]) -> [('task1', 2), ('task2', 1)]
    """
    if not validate_task_input(tasks) or not validate_priority_input(priorities):
        return []
    return [(task, priority) for (task, priority) in sorted(zip(tasks, priorities), key=lambda x: x[1], reverse=True)]