import os
import json
import progressbar

from multiprocessing import Pool
from logging import getLogger

from relate import entity_pairs_relatedness


logger = getLogger(__name__)


def tagme_relatedness(dataset_dir, output_dir):
    """
    Enhances each document of documents_dir with the relatedness between its
    entity pairs and saves them into a json file in output_dir.
    """
    documents = [name for name in os.listdir(dataset_dir) if name.endswith('json')]

    logger.info('{0} documents read from {1}'.format(len(documents), dataset_dir))

    errors = 0
    bar = progressbar.ProgressBar()
    for doc_name in bar(documents):
    	# Absolute filenames
    	input_filename = os.path.join(dataset_dir, doc_name)
    	output_filename = os.path.join(output_dir, doc_name)

        # Loads and annotate with entity pair relatedness.
    	annotated_document = json.load(open(input_filename, 'r'))
        relatedness = entity_pairs_relatedness(annotated_document)

        if relatedness is None:
            logger.error('Relatedness errors for document {0}. Skipped.'.format(input_filename))
            errors += 1
            continue

    	annotated_document['relatedness'] = relatedness


        outdir = os.path.dirname(output_filename)
        if not os.path.exists(outdir):
            os.makedirs(outdir)

    	json.dump(annotated_document, open(output_filename, 'w'), indent=4, sort_keys=True)


    if errors > 0:
        logger.warning('{0} documents have been skipped because annotation errors.'.format(len(errors)))

    logger.info('Relatedness Computation for directory {0} ended.'.format(dataset_dir))
