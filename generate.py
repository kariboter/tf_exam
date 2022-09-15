import torch
import os
from utils import preprocessing, parameter_parser_generate, predict
from src import Model

if __name__ == '__main__':

    args = parameter_parser_generate()
    dataset = preprocessing.Dataset(args)
    model = Model(dataset)
    prediction = "model path doesn't exist"
    if os.path.exists(args.model):
        model.eval()
        model.load_state_dict(torch.load(args.model))
        prediction = predict(dataset, model, text=args.prefix)
    print(prediction)