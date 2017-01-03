from duc import DUCDataset

def make_dataset(dataset_name):
	"""
	Factory-style method for getting dataset from string name.
	"""
	return {

		'duc': DUCDataset()

	}[dataset_name]
