import argparse

import pandas as pd
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description='Quickly visualize data from a text file.')
    parser.add_argument('path', type=str, help='Path to the file that should be plotted.')
    parser.add_argument('--columns', '-c', dest='columns', help='The column(s) that should be plotted, either as column index or,' +  
                                                                'if the file contains headers, column name.',
                        default=None, nargs='+')
    parser.add_argument('--no-headers', dest='header', action='store_false')
    parser.add_argument('--delimiter', '-d', dest='delimiter', help='The delimiter used in the file. Default: ","',
                        default=',')
    parser.add_argument('--index-col', dest='index_col', help='The index column of the data file.',
                        default=None)
    parser.add_argument('--type', '-t', dest='type', help='The type of plot to be produced. Default: Line plot.',
                        choices=['line'], default='line')

    return parser.parse_args()


def load_data(path, delimiter=',', header=None, index_col=None):
    try:
        index_col = int(index_col)
    except (ValueError, TypeError):
        pass

    data = pd.read_csv(path, delimiter=delimiter, header=0 if header else None, index_col=index_col)
    data = data.rename(columns=lambda x: x.strip())

    return data


def plot(data, columns, type='line'):
    plotted_data = pd.DataFrame()
    for i, column in enumerate(columns):
        try:
            c = int(column)
            plotted_data[data.columns[c]] = data.iloc[:, c]
        except ValueError:
            plotted_data[column] = data[column]

    plotted_data.plot()
    plt.show()
    plt.close()


def main():
    args = parse_args()
    data = load_data(args.path, args.delimiter, args.header, args.index_col)
    plot(data, args.columns, args.type)

if __name__ == '__main__':
    main()
