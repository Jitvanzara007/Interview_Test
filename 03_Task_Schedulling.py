'''
first priority is deadline so sorted it  
Then loop through the sorted list and keep allocating time
to tasks as long as total time does not exceed the deadline of the current task.
then just added completed task.
'''




def schedule(tasks):
    # sort by deadline first
    tasks.sort(key=lambda x: x['deadline'])

    time = 0
    selected_tasks = []

    for t in tasks:
        if time + t['duration'] <= t['deadline']:
            selected_tasks.append(t['name'])
            time += t['duration']

    return selected_tasks

tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

result = schedule(tasks)
print("Maximum tasks that can be completed:", result)

