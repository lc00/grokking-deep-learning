weight = 0.0
goal_pred = 0.8
input = 3
alpha = 0.1

for iteration in range(20):
  error = (input * weight - goal_pred) ** 2
  derivative = (input * weight - goal_pred) * input
  weight = weight - derivative * alpha
  print('Iteration:' + str(iteration))
  print("Error:" + str(error) + " Derivative:" + str(derivative))
  print('-------------')
