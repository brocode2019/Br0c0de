import json
import numpy as np
import cv2

from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

DICTION_FILE ='./dictionary.vocab'
MAX_LENGTH = 48  ##Input size that the model will take

class Plr:

    def __init__(self, model_json_path=None, model_weights_path=None):
        self.tokenizer, self.vocab_size = self.load_vocab()
        self.model = self.load_model(json_path,weights_path)

    def convert_image(self, output_path, png_path, verbose, style):
        png_filename = os.path.basename(png_path)
        if png_filename.find('.png') == -1:
            raise ValueError("Please Provide a PNG Image")
        input_image = png_filename[:png_filename.find('.png')]
        print("Generating Computer code for given Image:{}".format(input_image))
        generated_gui, gui_output_filepath= self.get_gui(png_path,verbose=verbose, output_path=output_path, input_image=input_image)
        


    def load_model(self, json_path,weights_path):
        json_file = open(model_json_path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(model_weights_path)
        
        return loaded_model

    def get_gui(self, png_path, verbose, input_image, output_path):
       
        img_features = self.get_img_features(png_path)

        initial_gui = '<START> '
        input_array = np.array([img_features])
        for i in range(150):
            sequence = self.tokenizer.texts_to_sequences([in_text])[0]
            sequence = pad_sequences([sequence], maxlen=MAX_LENGTH)
            prediction = self.model.predict([input_array, sequence], verbose=0)
            prediction = np.argmax(prediction)
            predicted_word = self.word_for_id(prediction)
            if predicted_word is None:
                break
            initial_gui += word + ' '
            if predicted_word == '<END>':
                break

        generated_gui = initial_gui.split()

        if verbose is 1:
            print("\n++++++++\nGenerated GUI code:")
            print(generated_gui)

        gui_output_filepath = self.save_gui_to_disk(generated_gui, sample_id, output_folder)

        return generated_gui, gui_output_filepath    

    def load_vocab(self):
        diction_file = open(DICTION_FILE, 'r')
        words = diction_file.read().splitlines()[0]
        diction_file.close()
        tokenizer = Tokenizer(filters='', split=" ", lower=False)
        tokenizer.fit_on_texts([words])
        return tokenizer

    def get_img_features(self, png_path):
        resized_img = self.resize_img(png_path)
        assert(resized_img.shape == (256,256,3))
        return resized_img

    def resize_img(self, png_path):
        rgb_img = cv2.imread(png_path)
        grey_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
        threshold_img = cv2.adaptiveThreshold(grey_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 101, 9)
        repeated_img = np.repeat(threshold_img[...,None],3,axis=2)
        resized_img = cv2.resize(repeated_img, (200,200), interpolation=cv2.INTER_AREA)
        all_ones_img = 255 * np.ones(shape=(256,256,3))
        all_ones_img[27:227, 27:227,:] = resized_img
        all_ones_img /= 255
        return all_ones_img








