#!/usr/bin/env python
import argparse
import json
import kseval.models

from datetime import timedelta
from kseval.utils import parse_date
from kseval.models.base import iterate_dataset
from operator import attrgetter
from math import exp
from datetime import datetime, timezone

#export KSEVAL_DATASETS="/home/landfried/meta/membership/licar/licar/papers/2020_TTT/experiment/input/data/"


## Tennis

cls = attrgetter('tennis.AffineWienerModel')(kseval.models)
config_path = "/home/landfried/meta/membership/licar/licar/papers/2020_TTT/experiment/input/data/input-eval/tennis-affine-wiener.json"
with open(config_path) as f:
    kwargs = json.load(f)
model = cls(**kwargs)
converged = model.fit()

## Basket

cls = attrgetter('basketball.DynamicModel')(kseval.models)
config_path = "/home/landfried/meta/membership/licar/licar/papers/2020_TTT/experiment/input/data/input-eval/basketball-matern12.json"
with open(config_path) as f:
    kwargs = json.load(f)

model = cls(**kwargs)
converged = model.fit()
0.53108 > exp(model.log_likelihood/(47342+20300))

## Chess


## Football

config_path = "../data/input-eval/football-matern12.json"
with open(config_path) as f:
    kwargs = json.load(f)

cls = attrgetter('football.DynamicModel')(kseval.models)
model = cls(**kwargs)
converged = model.fit(cutoff=datetime.strptime("2011-06-03", '%Y-%m-%d'))
exp(model.log_likelihood/13399)

fechas = []
for obs in iterate_dataset("kdd-football.txt"):
    fechas.append(datetime(datetime.fromtimestamp(obs["t"], timezone.utc).year, 1, 1))

date = []
n_obs = []
log_loss = []
for obs in iterate_dataset("eval/football-matern12.txt"):
    date.append(datetime.strptime(obs["date"], '%Y-%m-%d'))
    n_obs.append(obs["n_obs"])
    log_loss.append(obs["log_loss"])


cls = attrgetter('football.DynamicModel')(kseval.models)
model = cls(**kwargs)
converged = model.fit(cutoff=date[0])
n_obs_t, log_loss_t, accuracy_t = model.evaluate(begin=date[0], end=date[0]+timedelta(days=1))
log_loss[0]

converged = model.fit()
0.394222 > exp(model.log_likelihood/(13399 + 5759))



