# AdaptiveTest
Adaptive Test project in python

This application successively selects questions for the purpose of maximizing the precision of the exam based on what is known about the examinee from previous questions. For example, if an examinee performs well on an item of intermediate difficulty, they will then be presented with a more difficult question. Or, if they performed poorly, they would be presented with a simpler question. This application would be greatly helpful in the placement preparation process also and to access them on an equal scale. 

The basic computer-adaptive testing method is a simple iterative algorithm with the following steps: 

1.The pool of available items is searched for the optimal item, based on the current estimate of the examinee's ability 

2.The chosen item is presented to the examinee, who then answers it correctly or incorrectly 

3.The ability estimate is updated, based upon all prior answers 

4.Steps 1–3 are repeated until a termination criterion is met or a certain number of questions is reached. 
