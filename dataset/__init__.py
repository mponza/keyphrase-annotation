from duc import DUCDataset
from icsi import ICSIASRDataset, ICSIHumanTranscriptDataset
from inspec import InspectTrainingDataset, InspectValidationDataset, \
                    InspectTestDataset
from nus import NUSDataset


def make_dataset(dataset_name):
    """
    Factory-style method for getting dataset from string name.
    """
    return {

        'duc': DUCDataset(),

        'icsi-asr': ICSIASRDataset(),
        'icsi-ht': ICSIHumanTranscriptDataset(),

        'inspec-train': InspectTrainingDataset(),
        'inspec-val': InspectValidationDataset(),
        'inspec-test': InspectTestDataset(),

        'nus': NUSDataset()

    }[dataset_name]
