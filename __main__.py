import logging
import baker

from dataset import make_dataset
from annotation import tagme_annotation


logger = logging.getLogger(__name__)


@baker.command
def annotate(dataset_name, output_dir, threads=None):
    """
    Annotates a dataset and save annotations into output_dir.
    """
    logger.info('Running annotation upon {0}...'.format(dataset_name))

    dataset = make_dataset(dataset_name)
    tagme_annotation(dataset, output_dir, threads)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    baker.run()