import os
import json
import codecs

from multiprocessing import Pool
from logging import getLogger

from annotator import annotate


logger = getLogger(__name__)


def tagme_annotation(dataset, outputdir, threads=None):
    """
    Annotates each document of dataset and save its annotations
    into a json file.
    """
    threads = 8 if threads is None else threads
    
    documents = [document for document in dataset]
    logger.info('{0} documents read.'.format(len(documents)))

    logger.info('Generating TagMe annotations...')
    annotations = Pool(8).map(annotate, documents)

    logger.info('Saving annotations into {0}'.format(outputdir))

    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    errors = []
    for document, doc_anns in zip(documents, annotations):
        if doc_anns is None:
            errors.append(document.name)
            continue

        json_doc = {'tagme': doc_anns}

        filename = os.path.join(outputdir, document.name + '.json')
        json.dump(json_doc, open(filename, 'w'), indent=4, sort_keys=True)

    if len(errors) > 0:
        logger.warning('{0} documents have been skipped because annotation errors.'.format(len(errors)))
