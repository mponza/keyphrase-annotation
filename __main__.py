import os
import logging
import baker

from dataset import make_dataset
from annotation import tagme_annotation
from utils.output import DATA_OUTPUT


logger = logging.getLogger(__name__)


@baker.command
def annotate(dataset_name, output_dir, threads=None):
    """
    Annotates a dataset and save annotations into output_dir.
    """
    logger.info('Running annotation upon {0}...'.format(dataset_name))

    dataset = make_dataset(dataset_name)
    tagme_annotation(dataset, output_dir, threads)

    logger.info('Annotation for dataset {} ended.'.format(dataset_name))


@baker.command
def annotate_all(main_output_dir):
	for dataset_name, output_name in DATA_OUTPUT.items():
		output_dir = os.path.join(main_output_dir, output_name)
		annotate(dataset_name, output_dir)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    baker.run()