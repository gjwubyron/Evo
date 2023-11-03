import pandas as pd
import argparse 
from bert import BERTScore
from uncomet import COMET
import os

def set_scorer(metric, tgt_lang, test_mode=False):
    if metric == 'bert':
        scorer = BERTScore(tgt_lang, test_mode=test_mode)
    elif metric == 'comet':
        scorer = COMET(test_mode=test_mode)
    else:
        raise NotImplementedError
    return scorer

def get_score(scorer, src_lang, tgt_lang, metric, data_path, output_path):
    df = pd.read_csv(f'{data_path}/{src_lang}-{tgt_lang}.csv')
    source = df['source'].tolist()
    target = df['target'].tolist()
    score_df = pd.DataFrame()

    for date in df.iloc[:, 2:]:
        sys_output = df[date].tolist()
        sentence_score = scorer.score(source, target, sys_output)
        score_df[date] = sentence_score
    
    if not os.path.exists(f'{output_path}/{metric}'):
        os.makedirs(f'{output_path}/{metric}')
    score_df.to_csv(f'{output_path}/{metric}/{src_lang}-{tgt_lang}.csv', index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--metric', type=str, default='bert', help='metric to use')
    parser.add_argument('--data_path', type=str, default='evo_data', help='data path')
    parser.add_argument('--output_path', type=str, default='result', help='output path')
    parser.add_argument('--test', action='store_true', help='test mode')
    args = parser.parse_args()

    languages = ['en', 'de', 'es', 'it', 'zh']

    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    if args.metric != 'bert':
        scorer = set_scorer(args.metric, 'en', args.test)

    for tgt_lang in languages:
        if args.metric == 'bert':
            scorer = set_scorer(args.metric, tgt_lang, args.test)

        for src_lang in languages:
            if tgt_lang == src_lang:
                continue
            print(f'{src_lang} to {tgt_lang}')
            get_score(scorer, src_lang, tgt_lang, args.metric, args.data_path, args.output_path)
            
if __name__ == "__main__":
    main()