tasks = {

}

completedTasks = {

}

class taskFunctions:
    def addTask(task, description):
        taskExists = False

        for currentTask in tasks.keys():
            if currentTask == task:
                taskExists = True
                print('repeated tasks are not allowed!')
                break
    
        if not taskExists:
            tasks[task] = task
            
    def removeTask(task):
        taskExists = False

        for currentTask in tasks.keys():
            if currentTask == task:
                taskExists = True
                del tasks[task]
                break
    
        if not taskExists:
            print('task doesnt exist')
            
    def markTaskAsComplete(task):
        tasks_to_remove = []

        for currentTask in tasks.keys():
            if currentTask == task:
                completedTasks[task] = tasks[task]
                tasks_to_remove.append(currentTask)
                print(f'Task "{task}" marked as complete.')

        for task_to_remove in tasks_to_remove:
            del tasks[task_to_remove]

        if not any(currentTask == task for currentTask in tasks.keys()):
            print(f'Task "{task}" not found in the task list.')


    def listAllTasks():
        for task_title, task_description in tasks.items():
            print(f'Task: {task_title}, Description: {task_description}')
    
    def listAllCompletedTasks():
        for task_title, task_description in completedTasks.items():
            print(f'Completed Task: {task_title}, Description: {task_description}')

class usefulFunctions:
    def makeWhiteSpace(amount):
        for x in range(1, amount):
            print("")
            
    def workoutWord(words):
        return ' '.join(words[2:])

while True:
    usefulFunctions.makeWhiteSpace(3)
    print('type task add (task) to add a task')
    print('type task remove (task) to remove a task')
    print('type task list to list all tasks')
    print('type task complete followed by the task to complete the task')
    print('type task completed to list all completed tasks')

    userinput = input('enter the desired function here: ')
    words = userinput.split()

    if words[0] == 'task' and words[1] == 'add':
        taskToAdd = usefulFunctions.workoutWord(words)
        print()
        print(f'Adding task: "{taskToAdd}"')
        taskFunctions.addTask(taskToAdd, 0)
        
    elif words[0] == 'task' and words[1] == 'list':
        taskFunctions.listAllTasks()
        
    elif words[0] == 'task' and words[1] == 'remove':
        taskToRemove = usefulFunctions.workoutWord(words)
        print(f'Removing task: "{taskToRemove}"')
        taskFunctions.removeTask(taskToRemove)
        
    elif words[0] == 'task' and words[1] == 'complete':
        taskToComplete = usefulFunctions.workoutWord(words)
        taskFunctions.markTaskAsComplete(taskToComplete)
        print(f'Task Successfully completed: "{taskToComplete}"')
        
    elif words[0] == 'task' and words[1] == 'completed':
        taskFunctions.listAllCompletedTasks()