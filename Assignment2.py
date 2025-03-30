# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    
    biggest = 0

    for i in range( 1, len(numbers)):
 
      if numbers[i] > numbers[biggest]:
        biggest = i

    biggestvalue = numbers[biggest]
    filtered_numbers = numbers[:]
    filtered_numbers.remove(biggestvalue) 
    

    second_biggest = 0

    for i in range(0, len(filtered_numbers)):

      if filtered_numbers[i] == biggestvalue:
        second_biggest = i + 1
      if filtered_numbers[i] > filtered_numbers[second_biggest] and filtered_numbers[i] < biggestvalue:
        second_biggest = i
      

    if len(numbers) < 2:
      return numbers[biggest], None

    return numbers[biggest] , filtered_numbers[second_biggest]

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_numbers = sorted(set(numbers))
    return unique_numbers

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
  for i in range (1, len(arr)):
    arr[i] = arr[i] + arr[i - 1]
  return arr  

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
  rows = len(matrix)
  cols= len(matrix[0])
  transposed = [[0] * rows for _ in range (cols)]

  for i in range (rows):
    for j in range (cols):
      transposed[j][i] = matrix[i][j]
  return transposed

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
  i = 0 
  new_lst = [lst[0], ]
  for i in range (1, len(lst)):
    if i % step == 0:
      new_lst.append(lst[i])

  return new_lst

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
  for i in range (len(list1)):
    list1[i] *= list2[i]
  return sum(list1)

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
  result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
  for i in range (len(matrix1)):
    for j in range (len(matrix1[0])):
      for k in range (len(matrix2[0])):
        result[i][j] += matrix1[i][k] * matrix2[k][j]
  return result