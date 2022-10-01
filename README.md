# RGB CUBE working journal

This project is targeted at mimicking 3D object on three vertical LED planes.



# Day1

1. Buy some components needed.(74HCT245)

2. Look up documents for algorithms:

   [2D ray casting](https://www.youtube.com/watch?v=TOEi6T2mtHo&ab_channel=TheCodingTrain)

   [raycasting results tackling](https://www.youtube.com/watch?v=Vihr-PVjWF4&ab_channel=griffpatch)

   [collision detection](https://www.jeffreythompson.org/collision-detection/table_of_contents.php)

## Develop plan

1. Implement a ray casting in python.
2. Implement 3D rendering on one plane.
3.  transfer 3D rendering results in three vertical planes



Today I finished the basic frame for boundary construction and collision detection

# Day2

For multiple boundary detection, the ray shouldn't pierce the first boundary met, so it is necessary to return the distance of intersection point to choose the first collision point.

The current algorithm transverses the rays and boundaries, which seems to be of great complexity.

Add rectangle boundaries, this should be the body of the game map.

Though it will be interesting to add polygons or circle into the boundary type, it is more urgent to finish the 3D rendering, so my next step will be 3D rendering of the 2D results



# Day3

Made some code refactoring

To facilitate the debugging, write a map generator, which converts svg file to boundaries, the svg file can be got from draw.io

It is impossible to run two windows in pygame, so I will use network programming to communicate between to processes. Besides, I want to run the  game on PC, and transfer data to rpi.

On client, the 2D map is constructed, the raycasting algorithm will return every ray and its intersection with the boundary. The socket need to transfer tuple of ray angle and distance.

On server, the data from socket will be used to reconstruct 3D model. All walls' height will be set on a fixed value. 
$$
h = \frac{h_0}{d}
$$
 In our simple 3D model, the only problem to do determine:
$$
h = h(x) \\
d = d(x)
$$
h and d is related according to the above formula. The data from client is:
$$
d =d(\theta), \theta \in [-\theta_0, \theta_0]
$$
so we need to get
$$
x = x(\theta)
$$
Denote the x coordinate in client window is $l$
$$
l = d\sin \theta\\
l \in [-d_{left}\sin \theta_0, d_{right}\sin\theta_0]
$$
There is a linear mapping from client window to server window:
$$
x = al + b, x \in [0, D]
$$
so we get
$$
x = \frac{D}{(d_{left}+d_{right})\sin \theta_0 } l + \frac{Dd_{left}}{d_{left} + d_{right}}
$$


Finally, our 3D reconstruction algorithm will be:

1. Transverse $(\theta,d)$, calculate the counterpart of $(x, h)$
2. Draw rectangle with fixed width(An accurate calculation of $\Delta w$ will be slow and not much significant)

















































