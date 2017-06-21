import argparse
import os
import pickle
import sys

import numpy as np
from ml.TableExtractML import TableExtractorML
from TreeExtract import TreeExtractor
from TreeVisualizer import TreeVisualizer

def load_model(model_path):
    print "Loading pretrained model for table detection"
    model = pickle.load(open(model_path, 'rb'))
    print "Model loaded!"
    return model

def visualize_tree(pdf_file, pdf_tree):
    v = TreeVisualizer(pdf_file)
    a = v.display_candidates(pdf_tree)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="""Script to extract tree structure from PDF files.""")
    parser.add_argument('--model_path', type=str, default=None, help='pretrained model')
    parser.add_argument('--pdf_file', type=str, help='pdf file name for which tree structure needs to be extracted')
    args = parser.parse_args()
    model = None
    if (args.model_path is not None):
        model = load_model(args.model_path)
    extractor = TreeExtractor(args.pdf_file)
    if(not extractor.is_scanned()):
        print "Document is not scanned, building tree structure"
        pdf_tree = extractor.get_tree_structure(model)
        imgs = visualize_tree(args.pdf_file, pdf_tree)
    else:
        print "Document is scanned, cannot build tree structure"