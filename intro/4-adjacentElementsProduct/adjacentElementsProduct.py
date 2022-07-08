def solution(inputArray):
  return max(x*y for x, y in zip(inputArray, inputArray[1:]))
