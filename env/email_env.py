from env.tasks import tasks
from env.grader import grade

class EmailEnv:
    def __init__(self):
        self.current_task = None
        self.step_count = 0
        self.done = False

    def reset(self):
        self.step_count = 0
        self.done = False
        self.current_task = tasks[self.step_count]
        return self._get_obs()

    def _get_obs(self):
        return {
            "email": self.current_task["email"],
            "sender": self.current_task["sender"]
        }

    def step(self, action):
        self.step_count += 1

        reward = grade(self.current_task, action)
        done = True if reward == 1.0 else False

        info = {
            "task": self.current_task["name"],
            "error": None if reward > 0 else "wrong_action"
        }

        return self._get_obs(), reward, done, info

    def state(self):
        return self.current_task