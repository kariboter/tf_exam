import argparse

def parameter_parser():

    parser = argparse.ArgumentParser(description="Text Generation")
    parser.add_argument('--sequence_length', type=int, default=5)
    parser.add_argument("--epochs", dest="epochs", type=int, default=5)
    parser.add_argument("--batch_size", dest="batch_size", type=int, default=256)
    parser.add_argument("--load_model", dest="load_model", type=bool, default=False)
    parser.add_argument("--model", dest="model", type=str, default='data/textGenerator_model.pt')

    return parser.parse_args()

