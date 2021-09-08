import numpy as np
import keras
import sys
import os


def save_csv(dir, filename, data):
    '''
    Join the directory path with the filename and save the data as a .CSV file
    :param dir: parent directory (your_model_directory/csv_parameters/) in this case
    :param filename: name of the .CSV file
    :param data: data to be saved as a .CSV
    :return:
    '''
    file = os.path.join(dir, filename)
    np.savetxt(file, w, delimiter=",")


if __name__ == '__main__':
    # When launching the script, add the path of the model you want to convert as an argument
    try:
        model_path = sys.argv[1]
        print("Loading model " + os.path.basename(model_path) + "...")
    except:
        # model_path = "/path/to/your/model"  # manually insert path in the script. If so, comment out the following two lines
        print('No model found. Double check path.')
        sys.exit(1)  # exit program

    nn_model = keras.models.load_model(model_path) # load NN model
    csv_dir = os.path.dirname(model_path) + "/csv_parameters" # create directory to save the .csv files
    print("Creating /csv_parameters directory in the model's directory...")
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)

    for num, layer in enumerate(nn_model.layers):
        print("--- LAYER", num, " ---")
        w = layer.get_weights()[0]
        w_filename = "w" + str(num) + ".csv"
        save_csv(csv_dir, w_filename, w)
        print("...weights printed to " + w_filename)
        b = layer.get_weights()[1]
        b_filename = "b" + str(num) + ".csv"
        save_csv(csv_dir, b_filename, b)
        print("...biases printed to " + b_filename)
