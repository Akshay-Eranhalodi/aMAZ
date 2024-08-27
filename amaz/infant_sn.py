#!/usr/bin/env python3

import yaml 
from astropy.time import Time
import datetime
from argparse import ArgumentParser

def job_gen(date=None, deltat=1, mindet=1, maxdet=8):
    
    if not date:
        date = datetime.date.today()
        
    print(date)
        
    template = './template/infant_sn.yml'
    with open(template, 'r') as base:
        with open('./jobfiles/infant_sn.yml', 'w') as op_f:
                
                data = yaml.load(base, Loader=yaml.FullLoader)
                
                print(data['parameters'])

                data['parameters'][0]['value'] = str(date)
                data['parameters'][1]['value'] = str(date)
                data['parameters'][2]['value'] = deltat
                data['parameters'][3]['value'] = mindet
                data['parameters'][4]['value'] = maxdet
                print(data['parameters'])
                
                print(datetime.date.today())
                yaml.dump(data, op_f, sort_keys=False)

    
if __name__=="__main__":
    
    parser = ArgumentParser()

    parser.add_argument(
        "--date", "-s",
        type=str,
        help="Start date in the format 'yyyy-mm-dd' ",
        default = f"Current date: {datetime.date.today()}"
    )
    parser.add_argument(
        "--daysago", "-d",
        type=str,
        help="Start date",
        default="1"
    )
    parser.add_argument(
        "--mindet", "-min",
        type=str,
        help="minimum number of detections",
        default="1"
    )
    parser.add_argument(
        "--maxdet", "-max",
        type=str,
        help="maximum number of detections",
        default="8"
    )
    print(parser.parse_args())
    print(vars(parser.parse_args()))
    # print(parser.parse_args().args())
    print(datetime.date.today())

    # job_gen()