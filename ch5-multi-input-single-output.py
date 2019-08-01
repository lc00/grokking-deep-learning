toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

inputs = [toes[0], wlrec[0], nfans[0]]
weights = [0,0,0]
delta = [0,0,0]
weight_deltas = [0,0,0]

win_or_lose_binary = [1,1,0,1]
true = win_or_lose_binary[0]

alpha = 0.01

def neural_network(inputs, weights):
  prediction = 0
  for i in range(3):
    prediction += inputs[i] * weights[i]

  return prediction

def ele_mul(delta, inputs):
  # result_weight_delta = 0

  for i in range(3):
    weight_deltas[i] = inputs[i] * delta * alpha
    # result_weight_delta -= weight_deltas[i]

  return weight_deltas





for i in range(100):
  prediction = neural_network(inputs, weights)
  error = (prediction - true) ** 2
  delta = prediction - true
  weight_deltas = ele_mul(delta, inputs)
  weight_deltas[0] = 0

  print('Error: ' + str(error) + " Prediction: " + str(prediction))
  print('delta: ' + str(delta) + " weight_deltas: " + str(weight_deltas))
  print('-------------')

  for j in range(3):
    weights[j] -= weight_deltas[j]

print('Error: ' + str(error) + " Prediction: " + str(prediction))
print('delta: ' + str(delta) + " weight_deltas: " + str(weight_deltas))

