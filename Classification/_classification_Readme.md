## Quick Details on the classification
The model I built is based on an example from the TF docs on classication of a movie (good or bad) based on the text of the review.
Using the already built nnlm-en-dim128, which tokenizes text(turns into encoded numbers), and changing from binary to sparse 
categorical, I was able to create the supervised model for multiclass inputs. I spent a lot of time just getting stuff to fit,
since I was using custom data from our crawler. 

After the incredibly tedious parrallelized web crawling which is all credit to my teammates. I used pandas to pull the two features I needed
'product_name' and 'product_category'

![data cleaning](https://github.com/srishtis/TAMU-Datathon/blob/main/Classification/Data_Preproccessing.png)
![model flow](https://github.com/srishtis/TAMU-Datathon/blob/main/Classification/Model_Process.png)

Then I train to ~90% accuracy which was about 30 epochs

After this, all that was left was the front end. Not that it was trivial, perhaps opposite of that...
