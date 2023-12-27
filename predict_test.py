# -*- coding: utf-8 -*-
import tensorflow as tf
import tensorflow_text as text

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
gpus = tf.config.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only use the first GPU
  try:
    tf.config.set_visible_devices(gpus[0], 'GPU')
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
  except RuntimeError as e:
    # Visible devices must be set before GPUs have been initialized
    print(e)

def print_my_examples(inputs, results):
  result_for_printing = \
    [f'input: {inputs[i]:<30} : score: {results[i][0]:.6f}'
                         for i in range(len(inputs))]
  print(*result_for_printing, sep='\n')
  print()

examples = [
    'The demarcation line should be 38 latitude', #a provisional ex of NK talk
    'our proposal of fixing the 38th Parallel is completely inflexible', #NK
    'we propose the present battle line for demarcation', #UN,
    'We propose the current line of contact as delimitarized zone', #UN
    'we have proposed making the 38th Parallel the military demarcation line', #NK
    'the prisoners of war return back according to their nation',#a provisional ex of NK talk
    'the prisoners of war go to countries of their choice',#a provisional ex of UN talk
    'the international law treats the prisoners of war', #a provisional ex of UN talk
    'the Red Cross representatives visit the prisoners of war camp' #a provisional ex of UN talk
    ]

dataset_name = 'armistice_talk'
saved_model_path = './{}_bert_cased_large'.format(dataset_name.replace('/', '_'))
print(saved_model_path)
reloaded_model = tf.saved_model.load(saved_model_path)#XXX

reloaded_results = tf.sigmoid(reloaded_model(tf.constant(examples)))
print('Results from the saved model:') #prob. of be NK speakings.
print_my_examples(examples, reloaded_results)
