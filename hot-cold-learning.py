weight = 0.0
goal_pred = 0.8
input = 10



alpha = 0.001

for iteration in range(20):
  error = (input * weight - goal_pred) ** 2
  derivative = (input * weight - goal_pred) * input

  print('Iteration:' + str(iteration))
  print("Error:" + str(error) + " Weight:" + str(weight)  + " Derivative:" + str(derivative))

  test = input * weight
  print("input * weight: " + str(test))
  print('-------------')

  weight = (weight - derivative) * alpha
  
