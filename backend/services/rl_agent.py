import gym
from gym import spaces
import numpy as np
from stable_baselines3 import PPO

# Example: RL Environment for Material Selection
class MaterialSelectorEnv(gym.Env):
    def __init__(self, materials):
        super().__init__()
        self.materials = materials
        self.action_space = spaces.Discrete(len(materials))
        self.observation_space = spaces.Box(low=0, high=1, shape=(len(materials),), dtype=np.float32)
        self.state = np.zeros(len(materials))
        self.current_step = 0

    def reset(self):
        self.state = np.zeros(len(self.materials))
        self.current_step = 0
        return self.state

    def step(self, action):
        # Reward logic: +1 for selecting a sustainable material, -1 otherwise
        reward = 1 if self.materials[action]["sustainability"] > 7 else -1
        self.state[action] = 1
        self.current_step += 1
        done = self.current_step >= 10
        info = {}
        return self.state, reward, done, info

# Example material data
materials = [
    {"name": "Steel", "sustainability": 5},
    {"name": "Bamboo", "sustainability": 9},
    {"name": "Plastic", "sustainability": 3}
]

env = MaterialSelectorEnv(materials)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000)

# Inference: Get recommended material index
def recommend_material(user_state):
    action, _states = model.predict(user_state)
    return materials[action]

# FastAPI endpoint example
from fastapi import APIRouter, Request

rl_router = APIRouter()

@rl_router.post("/plan_rl")
async def plan_rl(request: Request):
    payload = await request.json()
    user_state = np.array(payload.get("state", [0,0,0]))
    recommendation = recommend_material(user_state)
    return {"recommended_material": recommendation["name"], "properties": recommendation}
