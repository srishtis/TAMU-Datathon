import tensorflow as tf
import numpy as np
tf.keras.backend.clear_session()


# Takes in single raw string and runs prediction on it
def single_predict(raw_string_input):
    loaded_model = tf.keras.models.load_model('text_product_classify_7_cat')

    # get raw input from function input
    test_input = raw_string_input

    # perform prediction
    preds = loaded_model.predict([test_input])
    preds = preds.flatten()
    #print(preds)

    # get index of the highest percent prediction
    ind = np.unravel_index(np.argmax(preds, axis=None), preds.shape)
    ind = str(ind)
    ind = int(ind.strip("(),"))

    # We will need to find the term and get key
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
                  'Seasonal': 11,
                  'Industrial & Scientific': 12,
                  'Household Essentials':13,
                  'Shop by Brand': 14,
                  'Party & Occasions': 15,
                  'Baby': 16,
                  'Walmart for Business': 17,
                  'Books': 18,
                  'Shop by Movie': 19,
                  'Feature': 20,
                  'Movies & TV Shows': 21,
                  'Shop by TV Show': 22,
                  'Arts Crafts & Sewing': 23,
                  'Music': 24,
                  'Home Improvement': 25,
                  'Pets': 26,
                  'Patio & Garden': 27,
                  'Beauty': 28,
                  'Shop by Video Game': 29,
                  'Character Shop': 30,
                  'Health': 31,
                  'Video Games': 32,
                  'Clothing': 33,
                  'Services': 34
                  }

    # search our dictionary and return the category that maches highest prob index
    for product_name, product_number in label_dict.items():
        if product_number == ind:
            likely_category = product_name

    return likely_category


# # EXTRA FUNCTION CALL FOR TESTING, THIS WOULD BE CALLED IN MAIN UI LOOP
# raw_input_test = 'Cricket Wireless LG Risio 4 16GB Prepaid Smartphone, Blue'
# predictions, high_prob_category = single_predict(raw_input_test)
# print("With chosen input: " + raw_input_test)
# print("The most likely category is: " + high_prob_category)
