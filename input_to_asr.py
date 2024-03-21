import os
import nemo_asr


def batch():
    base_dir = '~/Documents/Computers/COS498/'
    model = nemo_asr.model(base_dir+'models/twi_v1')
    directory = base_dir+'/'
    output = []
    for fname in os.listdir(directory):
        with open('/'.join([directory, fname]), 'rb') as f:
            transcirption = model.transcribe(f)
            output.append(transcirption)

