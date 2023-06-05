import gym
import yaml
from gym.utils.play import play

from griddly import GymWrapperFactory

wrapper = GymWrapperFactory()

def string_into_YAML(str, filename, index = 0):
    with open(f"{filename}.YAML", 'r') as f:
        file = yaml.safe_load(f)
    
    file['Environment']['Levels'][index] = str

    with open(f"{filename}.YAML", 'w') as f:
        yaml.dump(file, f)

string_into_YAML("w w w w w w\nw g A . . w\nw . . . . w\nw . 1 1 . w\nw . k . . w","test")

wrapper.build_gym_from_yaml('BaitTest','test.yaml', level=2)

play(gym.make('GDY-BaitTest-v0'))

'''
env = gym.make('GDY-BaitTest-v0')
env.reset()

# Replace with your own control algorithm!
for s in range(1000):
    obs, reward, done, info = env.step(env.action_space.sample())
    env.render() # Renders the environment from the perspective of a single player
    env.render(observer='global') # Renders the entire environment

    if done:
        env.reset()
        '''