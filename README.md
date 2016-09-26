# toy-robot
An application to model a robot moving around on a table.

I got the idea to do this project for myself after I found:
Github user fredwu's toy-robot-elixir repository.


+   The application simulates a robot moving around on a tabletop of a given size.
+   The robot must be prevent from falling off the table.
+   Further movements are still allowed if valid.

The following commands are valid:
+   PLACE X,Y,F : puts the robot on the table at the given X,Y with the given Facing.
+   MOVE : moves the robot one unit forward in its facing direction.
+   LEFT : rotates the robot 90 degrees to the left.
+   RIGHT : rotates the robot 90 degrees to the right.
+   REPORT : gives the X,Y position and Facing of the robot.

The origin (0,0) is the southwest-most corner space.

For my program, the robot will follow the commands from a given text file.
