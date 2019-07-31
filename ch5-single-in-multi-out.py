wlrec = [0.65, 1.0, 1.0, 0.9]

hurt = [0.1, 0.0, 0.0, 0.1] 
win =[1, 1, 0,1] 
sad = [0.1, 0.0, 0.1, 0.2]

input = wlrec[0]
outputs = [hurt[0], win[0], sad[0]]

errors = [0,0,0]
deltas = [0,0,0]
weights = [1,1,1]
weight_deltas = [0,0,0]
predictions = [0,0,0]

alpha = 0.1

def neural_network(input, weights):
  for i in range(3):
    predictions[i] = input * weights[i]
  return predictions

def process():
  for i in range(len(outputs)):
    predictions = neural_network(input, weights)
    errors[i] = (predictions[i] - outputs[i]) ** 2
    deltas[i] = predictions[i] - outputs[i]
    weight_deltas[i] = input * deltas[i] 

    weights[i] -= weight_deltas[i] * alpha

    print('errors:' + str(errors))
    print('predictions:' + str(predictions))
    print('weights' + str(weights))
    print('weight_deltas' + str(weight_deltas))
    print('weights' + str(weights))
    print('--------------')
  return weights  

for i in range(50):
  process()


