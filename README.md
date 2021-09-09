
## Simple Neural Network 
A very simple script to export the parameters (i.e., weights, biases) of a saved Neural Network model (.h5) to .csv files, for later use.  
In this project, I use [Keras](https://www.tensorflow.org/guide/keras/save_and_serialize) to load the models, but it can be adapted according to your framework preference.
  
### How to run
Simply launch from the command line

    python main_nn_parameters_to_csv.py /path/to/your/model/mymodel.h5
    
   to export the weights and biases of the selected trained model to .csv formats.
   Alternatively, you can manually insert the path to your selected model into the script my modify the exception routine as follows :
   
```python
model_path = "/path/to/your/model"
# print('No model found. Double check path.')  
# sys.exit(1)  # exit program
```

This way, it won't quit the program when the arguments are null.

Two .csv files are generated for each layer (one for *weights* and one for *biases*) and saved into an auto-generated subfolder `/csv_parameters` inside the model's directory.

**Example .csv file for weights**

Assuming Layer 1 is a dense layer with 2 inputs and 3 outputs, the respective weights file `w1.csv`  would look like *(random numbers)*

    1.1266,5.5338,1.4371
    4.2968,5.6462,-5.3324

In which each row represents one of the inputs and each column the weight associated to each output neuron.
Intuitively, the biases file `b1.csv` will be

    -1.5581
     7.90840
     0.0000
 In which each row represents the bias  associated to each output neuron.
### Minimum working examples
In the repository you can find two pre-trained models: 
- A **regression model**, built using a NN with dimensions (8, 12, 8) 
- The **XOR model**, built using a NN with dimensions (2, 2, 1)

For the XOR example, there is also a simple script that allows you to generate your model (you can play around with the hyperparameters if you want). Then, you can test the functionality of the script by selecting your trained model.



