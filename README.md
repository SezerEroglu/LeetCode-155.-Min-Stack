# LeetCode-155.-Min-Stack

We keep an another minimum stack and append the newest minimum value as the stack gets appended.
If the appended value is not higher than the minimum, we add another minimum, simulating as if the pop operation did not change 
the minimum.