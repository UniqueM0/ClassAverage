

"""
input: the test scores 
initiate a iterator (counter) and accumulator (sum) and set it to zero 
loop through the list of test scores
add all the test scores
increment the counter by one
once the loop ends, there are no more scores to add
divide the accumulator (sum) by the counter 
display the output to the user
output: print the average of the class scores
"""

"""
scores
iterator, accumulator = 0
loop through scores
    accumulator = accumulator + scores 
    iterator = iterator + 1 
output = accumulator / total score
print output
"""

def calculate_average(scores):    
    # scores = [100, 80, 90, 70, 50, 95]  # input
    iterator = 0
    accumulator = 0
    student_count = len(scores)
    print("length is:", len(scores))

    while iterator < len(scores):
        # print("within while loop iterator: ", iterator)
        print(f"item at index {iterator} is: ", scores[iterator])
        accumulator = accumulator + scores[iterator]
        iterator = iterator + 1

    print("sum is: ", accumulator)
    average = accumulator / student_count
    # print("The average of total scores in the class is: ", average)
    return average

output = calculate_average([100,80,90,70,50,95])

print("The average of total scores in the class is: ", output)
