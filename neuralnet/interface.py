import torch

path = '/home/developer/workspace/hakaton-ml/neuralnet'

model = torch.hub.load(path, 'custom', source='local')

video = '/home/developer/workspace/hakaton-ml/dataset/images/000343.jpg'

results = model(video)

results.save()