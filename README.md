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

