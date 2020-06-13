#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) It is O(n). The function runs as many times as the input count is.


b) This is also O(n) since it will run the function as many times as the input count.


c) This would be O(2n) Exponential. It is a recursive return that runs more than double the input size. 

## Exercise II

### I would use a binary search alogorithm. 
- Take the total number of floors and find half. 
- Drop and egg and see if it breaks. 
- If it does then take the lower half and find half there. 
- Drop an egg again. 
- See if it breaks there. 
- If it does, then repeat finding half on the lower half of the floors. 
- Repeat this until you get an egg that doesn't break. 
- You should be able to determine the last floor at which eggs will break. 
- Then you will know that the floor below it will be the highest floor at which eggs won't break. 
- This should be O(log n) - Log Linear
