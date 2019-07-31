toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65,0.8, 0.8, 0.9] 
nfans = [1.2, 1.3, 0.5, 1.0]

hurt = [0.1, 0.0, 0.0, 0.1] 
win = [1,1,0,1] 
sad = [0.1, 0.0, 0.1, 0.2]

inputs = [toes[0], wlrec[0], nfans[0]]
outputs = [hurt[0], win[0], sad[0]]
predictions = [1, 1, 1]
alpha = 0.1

errors = [0,0,0]
deltas = [0,0,0]

weights = [ [0.1, 0.1, -0.3],# hurt?
            [0.1, 0.2, 0.0], # win?
            [0.0, 1.3, 0.1] ]# sad?
weight_deltas = [ [0.1, 0.1, -0.3],# hurt?
            [0.1, 0.2, 0.0], # win?
            [0.0, 1.3, 0.1] ]# sad?

def neural_network(inputs, weights):
  prediction = 0
  for i in range(len(weights)):
    prediction += inputs[i] * weights[i]
  return prediction

def multiplication_matrix(inputs, weights):
  for i in range(len(inputs)):
    predictions[i] = neural_network(inputs, weights[i])
  return predictions


def process(inputs, weights):
  for i in range(3):
    predictions[i] = neural_network(inputs, weights[i])
    errors[i] = (predictions[i] - outputs[i]) ** 2
    deltas[i]= predictions[i]- outputs[i]

    for j in range(3):
      weight_deltas[i][j] = inputs[i] * deltas[j]
      weights[i][j] -= weight_deltas[i][j] * alpha

      print('errors:' + str(errors))
      print('predictions:' + str(predictions))
      print('weight_deltas' + str(weight_deltas))
      print('weights' + str(weights))
      print('--------------')
  
  return weights 

# errors = [ [0,0,0],
#             [0,0,0],
#             [0,0,0]]

# deltas = [ [0,0,0],
#             [0,0,0],
#             [0,0,0]]
# def process(inputs, weights):
#   for i in range(3):
#     predictions[i] = neural_network(inputs, weights[i])
#     for j in range(3):
#       errors[i][j] = (inputs[i] * weights[i][j] - outputs[i]) ** 2
#       deltas[i][j] = inputs[i] * weights[i][j] - outputs[i]
#       weight_deltas[i][j] = inputs[i] * deltas[i][j]
#       weights[i][j] -= weight_deltas[i][j] * alpha

#       print('errors:' + str(errors))
#       print('predictions:' + str(predictions))
#       print('weight_deltas' + str(weight_deltas))
#       print('weights' + str(weights))
#       print('--------------')
#   return weights[i]  

# for i in range(3):
process(inputs, weights)



  