from ResolveOutput import ResolveOutput
from Request import Request
import os


def run(source, weights_file, flags=''):
    outputs = []
    if not isinstance(source, str):
        raise ValueError('source param must be str')
    if not isinstance(weights_file, str):
        raise ValueError('weights_file param must be str')
    if not isinstance(flags, str):
        raise ValueError('flags param must be str')

    outputs = os.popen(f'python3 neuralnet/detect.py --source {source} --weights {weights_file} {flags} ')


    unloaded = 0
    near = 0
    for output in outputs:
        status = ResolveOutput.get_status(output)
        if status is 'unloaded':
            unloaded += 1
        elif status is 'is_near_can_or_in_can':
            near += 1

    status = ResolveOutput.resolve_status(unloaded, near)
    type = ResolveOutput.get_type(status)

    return status, type


if __name__ == '__main__':
    status, type = run('/home/developer/Downloads/vid_sample1.avi', 'neuralnet/best.pt', '--save-txt')
    print(status, type)
