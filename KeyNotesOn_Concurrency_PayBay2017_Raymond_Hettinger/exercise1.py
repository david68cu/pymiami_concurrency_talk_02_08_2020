counter = 0

def worker():
    'My job is to increment the counter and print the current count'
    global counter

    counter += 1
    print('The count is %d' % counter)
    print('---------------')



print('Starting up')
for i in range(10):
    worker()
print('Finishing up')

# OUTPUT

# Starting up
# The count is 1
# ---------------
# The count is 2
# ---------------
# The count is 3
# ---------------
# The count is 4
# ---------------
# The count is 5
# ---------------
# The count is 6
# ---------------
# The count is 7
# ---------------
# The count is 8
# ---------------
# The count is 9
# ---------------
# The count is 10
# ---------------
# Finishing up
