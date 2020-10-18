import tensorflow as tf
import numpy as np
import re


tf.keras.backend.clear_session()
# Takes in single raw string and runs prediction on it
def single_predict(raw_string_input):
    loaded_model = tf.keras.models.load_model('text_product_classify')

    # get raw input from function input
    test_input = raw_string_input

    # perform prediction
    preds = loaded_model.predict([test_input])
    preds = preds.flatten()
    print(preds)

    #get index of the highest percent prediction
    ind = np.unravel_index(np.argmax(preds, axis=None), preds.shape)
    ind = str(ind)
    ind = int(ind.strip("(),"))

    #We will need to find the term and get key
    label_dict = {'Food': 0,
                  'Electronics': 1,
                  'Personal Care': 2,
                  'Toys': 3,
                  'Home': 4,
                  'Gifts & Registry': 5,
                  'Cell Phones': 6,
                  'Office Supplies': 7,
                  'Auto & Tires': 8,
                  'Musical Instruments': 9,
                  'Sports & Outdoors': 10,
                  'Seasonal': 11
                  }

    # search our dictionary and return the category that matchest highest prob index
    for product_name, product_number in label_dict.items():
        if product_number == ind:
            likely_category = product_name

    return preds, likely_category


# EXTRA FUNCTION CALL FOR TESTING, THIS WOULD BE CALLED IN MAIN UI LOOP
raw_input_test = 'iphone xr'
predictions, high_prob_category = single_predict(raw_input_test)
print("With chosen input: " + raw_input_test)
print("The most likely category is: " + high_prob_category)
