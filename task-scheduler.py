class Task:
    PRIORITY_LEVELS = {"High":1, "Medium":2, "Low":3}

    def __init__(self, task_id, description, priority, completed=False):
        self.task_id = task_id
        self.description = description 
        if priority in self.PRIORITY_LEVELS:
            self.priority = priority 
        else:
            raise ValueError(f"Invalid priority: {priority}. Must be one of {list(self.PRIORITY_LEVELS.keys())}")
        self.completed = completed 
    
    def __str__(self):
        status = "Completed" if self.completed else "Not Completed" 
        return f"Task ID: {self.task_id}, Description: {self.description}, Priority: {self.priority}, Status: {status}"
        

class Taskscheduler:

    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, description, priority):
        task = Task(task_id, description, priority)
        self.tasks[task_id] = task 
        print(f"Task '{description}' added with ID {task_id}.")

    def mark_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].completed = True
            print(f"Task ID {task_id} marked as completed. ")
        
        else:
            print(f"Task ID {task_id} not found.")

    def get_next_task(self):
        if not self.tasks:
            print("No tasks available.")
            return None 
        
        next_task = None 

        for task in self.tasks.values():
            if not task.completed:
                if next_task is None or Task.PRIORITY_LEVELS[task.priority] < Task.PRIORITY_LEVELS[next_task.priority]:
                    next_task = task 
        
        if next_task:
            return next_task
        else: 
            print("No uncompleted tasks available. ")
            return None
        
    def get_all_tasks(self, sort_by_priority=False):
        if not self.tasks:
            print("No tasks available. ")
            return 
        tasks_list = list(self.tasks.values())

        if sort_by_priority:
            tasks_list.sort(key=lambda task: Task.PRIORITY_LEVELS.get(task.priority,0))
        
        for task in tasks_list:
            print(task)

    def remove_task(self, task_id):
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Task '{removed_task.description}' with ID {task_id} has been removed")
            
        else:
            print(f"Task ID {task_id} not found ")

scheduler = Taskscheduler()

scheduler.add_task(1, "Fix bug in code" , "High")
scheduler.add_task(2, "Write documentation", "Medium")
scheduler.add_task(3, "Deploy application", "Low")

print("\nAll Task: ")
next_task = scheduler.get_next_task()
if next_task:
    print(next_task)

scheduler.mark_completed(3)

print("\nNext Task After Marking Task 3 as Completed: ")
next_task = scheduler.get_next_task()
if next_task:
    print(next_task)

scheduler.remove_task(2)

print("\n All Tasks After Removing Task 2: ")
scheduler.get_all_tasks(sort_by_priority=True)