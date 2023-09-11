from .runner import Runner
from .runner_gnn import RunnerGNN



from .runner_magic import RunnerMagic
from .runner_baselines import RunnerBaseline
from collections import namedtuple
from .runner_ic3net import RunnerIcnet

from .runner_tiecomm import RunnerTiecomm
from .runner_default import RunnerDefualt

from .runner_hiercomm import RunnerHiercomm
from .runner_hiercomm_random import RunnerHiercommRandom
from .runner_hiercomm_competition import RunnerHiercommCompetition
from .runner_hiercomm_cooperation import RunnerHiercommCooperation







REGISTRY = {}
REGISTRY["ac_mlp"] = Runner
REGISTRY["ac_att"] = Runner
REGISTRY["ac_att_noise"] = Runner
REGISTRY["gnn"] = RunnerGNN

REGISTRY["tiecomm"] = RunnerTiecomm
REGISTRY["tiecomm_default"] = RunnerDefualt
REGISTRY["tiecomm_wo_inter"] = RunnerTiecomm
REGISTRY["tiecomm_wo_intra"] = RunnerTiecomm


REGISTRY["hiercomm"] = RunnerHiercomm
REGISTRY["hiercomm_random"] = RunnerHiercommRandom
REGISTRY["hiercomm_competition"] = RunnerHiercommCompetition
REGISTRY["hiercomm_cooperation"] = RunnerHiercommCooperation



REGISTRY["magic"] = RunnerMagic
REGISTRY["commnet"] = RunnerBaseline
REGISTRY["ic3net"] = RunnerIcnet
REGISTRY["tarmac"] = RunnerBaseline

# REGISTRY["gacomm"] = GACommAgent