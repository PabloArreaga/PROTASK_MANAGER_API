class SingletonStorage:
    _instance = None
    _tasks = []
    _next_id = 1

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonStorage, cls).__new__(cls)
        return cls._instance

    def get_next_id(self) -> int:
        task_id = self._next_id
        self._next_id += 1
        return task_id

    def add_task(self, task):
        self._tasks.append(task)

    def get_all_tasks(self):
        return self._tasks

    def get_task(self, task_id: int):
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, updated_task):
        for index, task in enumerate(self._tasks):
            if task.id == updated_task.id:
                self._tasks[index] = updated_task
                return

    def delete_task(self, task_id: int):
        self._tasks = [task for task in self._tasks if task.id != task_id]
