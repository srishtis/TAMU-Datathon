import tensorflow as tf


tf.keras.backend.clear_session()
# Takes in single raw string and runs prediction on it
def single_predict(raw_string_input):
    loaded_model = tf.keras.models.load_model('text_product_classify')

    test_input = 'XBOX ONE 1TB'
    preds = loaded_model.predict([test_input])
    print(preds)
    return preds

# EXTRA FUNCTION CALL FOR TESTING, THIS WOULD BE CALLED IN MAIN UI LOOP
single_predict('Pjjlaskjfdlakfj sdl;kfjdkl')
