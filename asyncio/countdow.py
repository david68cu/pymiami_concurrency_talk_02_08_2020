# countdown.py
# Simple generator function countdown.py
# David Beazley, reference [9]


def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1
    print("Done counting down")


# Example use
if __name__ == '__main__':
    for i in countdown(10):
        print(i)
