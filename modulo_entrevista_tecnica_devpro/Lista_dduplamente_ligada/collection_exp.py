from collections import deque

numbers = deque(range(5))
print(numbers)
print(f'len: {len(numbers)}')
print(f'pop: {numbers.pop()}, {numbers}')
numbers.appendleft(-1)
print(f'appendleft -1: {numbers}')
print(f'popleft: {numbers.popleft()}, {numbers}')
numbers.extend(range(4, 10))
print(f'extend range(4, 10): {numbers}')
numbers.extendleft(range(-1, -4, -1))
print(f'extendleft range(-1, -4, -1): {numbers}')

buffer = deque(maxlen=3)
print(buffer)
buffer.extend(range(3))
print(f'extend range(3): {buffer}')
buffer.append(3)
print(f'append 3: {buffer}')
buffer.appendleft(0)
print(f'appendlet 0: {buffer}')