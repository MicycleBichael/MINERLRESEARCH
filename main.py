import gym
from gym.utils.play import play

from griddly import GymWrapperFactory

wrapper = GymWrapperFactory()

wrapper.build_gym_from_yaml('BaitTest','test.yaml',level=1)

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