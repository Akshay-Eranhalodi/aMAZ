#!/usr/bin/env python3

import yaml
from astropy.time import Time
import datetime
from argparse import ArgumentParser


def job_gen(date, daysago, mindet, maxdet):
    isinstance(date, datetime.date)

    template = "./template/infant_sn.yml"
    with open(template, "r") as base:
        with open("./jobfiles/infant_sn.yml", "w") as op_f:
            data = yaml.load(base, Loader=yaml.FullLoader)

            data["parameters"][0]["value"] = str(date)
            data["parameters"][1]["value"] = str(date)
            data["parameters"][2]["value"] = daysago
            data["parameters"][3]["value"] = mindet
            data["parameters"][4]["value"] = maxdet

            yaml.dump(data, op_f, sort_keys=False)
    print("infant_sn.yml created successfully!")


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument(
        "--date",
        "-s",
        type=str,
        help="Start date in the format yyyy-mm-dd ",
        default=(datetime.date.today()),
    )
    parser.add_argument("--daysago", "-d", type=int, help="Start date", default=1)
    parser.add_argument(
        "--mindet", "-min", type=int, help="minimum number of detections", default=1
    )
    parser.add_argument(
        "--maxdet", "-max", type=int, help="maximum number of detections", default=8
    )
    cfg = vars(parser.parse_args())

    job_gen(**cfg)
