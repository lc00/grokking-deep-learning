#%%

vec_a = [8.5, 9]
vec_b = [0.1, 0]

def elementwise_multiplication (vec_a, vec_b):
  assert(len(vec_a) == len(vec_b))

  sum = 0

  for a, b in zip(vec_a, vec_b):
    sum += a * b
    return sum

def elementwise_addition (vec_a, vec_b):
  assert(len(vec_a) == len(vec_b))

  sum = 0

  for a, b in zip(vec_a, vec_b):
    sum += a + b
  return sum

def vector_sum(vec_a):
  sum = 0
  for a in vec_a:
    sum += a
  return sum

def vector_average (vec_a):
  sum = vector_sum(vec_a)  
  return sum / len(vec_a)
  
print('elementwise_multiplication', elementwise_multiplication(vec_a, vec_b))
print('elementwise_addition', elementwise_addition(vec_a, vec_b))
print('vector_sum', vector_sum(vec_a))
print('vector_average', vector_average(vec_a))





#%%
