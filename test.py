import numpy as np

def reward_fn(self, coord):
   """Calculate reward function according to section 4.1 in
   https://arxiv.org/abs/2106.04399.
   :param x_coord: (array-like) Coordinates
   :return: (float) Reward value at coordinates
   """
   assert len(coord) >= 1
   assert len(coord) == self.dim
   r1_term = 1
   r2_term = 1
   reward = self.r0
   for i in range(len(coord)):
      r1_term *= int(0.25<np.abs(coord[i]/(self.length-1)-0.5))
      r2_term *= int(
                 0.3 < np.abs(coord[i]/(self.length-1)-0.5)<= 0.4)
      reward += self.r1*r1_term + self.r2*r2_term
   return reward