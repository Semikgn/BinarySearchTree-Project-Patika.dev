#BinarySearchTree of: [7, 5, 1, 8, 3, 6, 0, 9, 4, 2] array

#Step 1:
#                       7 <-- Root
#                      /
#                     5  <-- 5 küçüktür 7

#Step2:
#                       7 
#                      /
#                     5
#                    /
#                   1   <-- 1 küçüktür 5 ve 7

#Step3
#                       7
#                      / \
#                     5   8 <-- 8 büyüktür 7
#                    /
#                   1

#Step4:
#                       7
#                      / \
#                     5   8
#                    /     
#                   1      
#                    \
#                     3 <-- 3 küçüktür 7 ve 5 ama büyüktür 1

#Step5:
#                       7
#                      / \
#                     5   8
#                    / \   
#                   1   6 <-- 6 küçüktür 7 ama büyüktür 5  
#                    \
#                     3
#                   
#Step6:
#                       7
#                      / \
#                     5   8
#                    / \   
#                   1   6   
#                  / \
#                 0   3   <-- 0 küçüktür 7, 5 ve 1

#Step7:
#                       7
#                      / \
#                     5   8
#                    / \   \
#                   1   6   9 <-- 9 büyüktür 7 ve 8
#                  / \
#                 0   3

#Step8:
#                       7 <-- Root
#                      / \
#                     5   8
#                    / \   \
#                   1   6   9
#                  / \
#                 0   3
#                      \
#                       4 <-- 4 küçüktür 7 ve 5 ancak büyüktür 1 ve 3

#Step9 (Last):
#                       7 <-- Root
#                      / \
#                     5   8
#                    / \   \
#                   1   6   9
#                  / \
#                 0   3
#                    / \
#                   2   4 <-- 2 küçüktür 7 ve 5 ancak büyüktür 1 ve küçüktür 3
