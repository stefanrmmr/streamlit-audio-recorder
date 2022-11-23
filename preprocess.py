import audio_utils
from matplotlib import pyplot as plt
from librosa.display import specshow
import io
import tensorflow as tf
import numpy as np

class AudioPreprocessor(object):
    def __init__(self):
        self.sr = 4000

    def preprocess(self, wav):
        #wav, sr = audio_utils.read_wav(filepath)
        #print(sr)
        splitted_wav = audio_utils.arr_split(wav, fs=self.sr, length=8, annotation=None, overlap=0.5)
        
        size = splitted_wav.shape[0]
        img_array = np.zeros((size,480,640,3))
        for idx, arr in enumerate(splitted_wav):

            log_mel = audio_utils.mel_log(arr)
            fig, ax = plt.subplots()
            plt.axis('off')  # no axis
            plt.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
            specshow(log_mel, sr=self.sr,fmax=self.sr/2) 
            # plt.savefig(image_folder + "/" + str(idx),  bbox_inches="tight", pad_inches=0)

            io_buf = io.BytesIO()
            fig.savefig(io_buf, format='rgba')
            io_buf.seek(0)
            img_arr = np.reshape(np.frombuffer(io_buf.getvalue(), dtype=np.uint8),
                        newshape=(int(fig.bbox.bounds[3]), int(fig.bbox.bounds[2]), -1))
            io_buf.close()  
            plt.close()
            img_arr = self.rgba2rgb(img_arr)
            img_array[idx,:] = img_arr   
        dataset = tf.convert_to_tensor(img_array)
        dataset = tf.image.resize(dataset, (224,224))
        dataset = tf.data.Dataset.from_tensor_slices(dataset)
        dataset = dataset.batch(32).prefetch(buffer_size=tf.data.AUTOTUNE)
        return dataset

    def rgba2rgb(self, rgba, background=(255,255,255) ):
        row, col, ch = rgba.shape

        if ch == 3:
            return rgba

        assert ch == 4, 'RGBA image has 4 channels.'

        rgb = np.zeros( (row, col, 3), dtype='float32' )
        r, g, b, a = rgba[:,:,0], rgba[:,:,1], rgba[:,:,2], rgba[:,:,3]

        a = np.asarray( a, dtype='float32' ) / 255.0

        R, G, B = background

        rgb[:,:,0] = r * a + (1.0 - a) * R
        rgb[:,:,1] = g * a + (1.0 - a) * G
        rgb[:,:,2] = b * a + (1.0 - a) * B

        return np.asarray( rgb, dtype='uint8' )