# Chess-AI
This is based on a decision tree with alpha beta pruning with an added twist. 

I do something interesting here, where a move that was one of many options is weighted as more than one layer in the decision tree and a move that is the only option is weighted as less than a layer in a decision tree. 

I use (number of options) / (average number of options) to represent how many levels to subtract from the recursive function's parameter. 

This allows the AI to find check mates in the end game much more easily once it starts cornering the king, it also allowed it to discover some standard openings with only three moves of look ahead because the options in the opening are more limited as well. 
