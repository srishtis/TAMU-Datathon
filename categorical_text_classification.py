import pandas as pd
import numpy as np

import tensorflow as tf
import tensorflow_hub as hub


if __name__ == "__main__":
    print('Executing Text analysis')
    # similar to a movie review example (good or bad based on text in review)
    # categorize product category based on the title of the product
    # web scraper gives us two features, product name and product parent breadcrumb
    # Train 20%, and then the 80% you will be able to determine label from description

    # defining some scope variables for later tuning
    num_samples = 20
    training_percent_split = .2
    validation_percent_split = .8

    # Assume data will come in via csv or json or some other pandas DF readable format
    # The drawback is that the data has to be in the same file
    df2 = pd.read_csv('big_df.csv')
    df = df2[['product_name', 'category_number']]

    #####################################
    # LOADING INTO A TF DATA SET BECAUSE THAT'S WAY EASIER
    ####################################

    # show first few rows as a sanity check
    print(df.head())

    # data splitting
    df['split'] = np.random.randn(df.shape[0], 1)
    msk = np.random.rand(len(df)) <= validation_percent_split

    train_data = df[msk]
    validation_data = df[~msk]

    train_data = (
        tf.data.Dataset.from_tensor_slices(
            (
                tf.cast(train_data['product_name'].values, tf.string),
                tf.cast(train_data['category_number'].values, tf.int8)
            )
        )
    )

    validation_data = (
        tf.data.Dataset.from_tensor_slices(
            (
                tf.cast(validation_data['product_name'].values, tf.string),
                tf.cast(validation_data['category_number'].values, tf.int8)
            )
        )
    )
    # modifying the TF docs example on movie reviews
    # Creating a layer that will tokenize and create the right output shape 'embedding' from text
    # don't know if this is capturing the whole string
    # using nnlm dim 50/2 but we can try other models
    embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
    hub_layer = hub.KerasLayer(embedding, input_shape=[], dtype=tf.string, trainable=True)

    # model layer definition (try with different activations although relu is usually best)
    model = tf.keras.Sequential()
    model.add(hub_layer)
    model.add(tf.keras.layers.Dense(16, activation='relu'))
    model.add(tf.keras.layers.Dense(35))
    model.summary()

    print('Are we compiling? ')
    # model compile, we need to use binary crossentropy for this with more categories
    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])



    print('Are we training? ')
    # model training
    history = model.fit(train_data.shuffle(num_samples).batch(512), epochs=30, validation_data=validation_data.batch(512), verbose=1)
    # history = model.fit(train_data, epochs=10, validation_data=validation_data, verbose=1)

    print('Are we evaluating? ')
    # model evaluation, still need to split some test data in here
    results = model.evaluate(train_data.batch(512), verbose=2)

    for name, value in zip(model.metrics_names, results):
        print("%s: %.3f" % (name, value))

    model.save('text_product_classify_9_cat')
