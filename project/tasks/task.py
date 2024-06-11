from logger import BaseLogger
from tqdm import tqdm
from io import StringIO
import sys

class Task:
    def __init__(self, name, action, logger: BaseLogger):
        self.name = name
        self.action = action
        self.dependencies = list()
        self.logger = logger

    def add_dependency(self, task):
        self.dependencies.append(task)

    def run(self):
        self.logger.info(f"Executing task: {self.name}")
        self.action()

class TaskPipeline:
    def __init__(self, name, logger: BaseLogger):
        self.name = name
        self.task = None
        self.logger = logger

    def __rshift__(self, next_task):
        self.add_task(next_task)
        return self

    def add_task(self, next_task):
        if self.task is None:
            self.task = next_task
        else:
            self._add_recursively(self.task, next_task)
        
    def _add_recursively(self, task, next_task):

        if isinstance(task, list):
            for parallel_task in task:
                if len(parallel_task.dependencies) == 0:
                    parallel_task.add_dependency(next_task)
                else:
                    for dependent_task in parallel_task.dependencies:
                        self._add_recursively(dependent_task, next_task)        

        else:
            if len(task.dependencies) == 0:
                task.add_dependency(next_task)
            else:
                for dependent_task in task.dependencies:
                    self._add_recursively(dependent_task, next_task)

    def run(self):
        if self.task:
            self.logger.info(f"[#] Pipeline at execution: {self.name}")
            self._run_recursively(self.task)
        else:
            self.logger(f"There are no tasks to run")

    def _run_recursively(self, task):
        if isinstance(task, list):
            for parallel_task in task:
                parallel_task.run()
                for dependent_task in parallel_task.dependencies:
                    self._run_recursively(dependent_task)
        else:
            task.run()
            for dependent_task in task.dependencies:
                self._run_recursively(dependent_task)

        
class PipelineQueue:
    def __init__(self):
        self.pipelines = []

    def push(self, pipeline):
        self.pipelines.append(pipeline)

    def run(self):
        stdout_backup = sys.stdout
        
        sys.stdout = StringIO()
        
        for pipeline in tqdm(self.pipelines, desc = 'Pipeline Queue Running'):
            pipeline.run()

        sys.stdout = stdout_backup