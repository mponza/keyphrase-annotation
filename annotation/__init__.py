import os
import json
import codecs

from multiprocessing import Pool
from logging import getLogger

from annotator import annotate


logger = getLogger(__name__)


def tagme_annotation(dataset, outputdir, threads=None):
    threads = 8 if threads is None else threads
    
    documents = [document for document in dataset]
    logger.info('{0} documents read.'.format(len(documents)))

    logger.info('Generating TagMe annotations...')
    annotations = Pool(8).map(annotate, documents)

    logger.info('Saving annotations into {0}'.format(outputdir))

    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    for document, doc_anns in zip(documents, annotations):
        if doc_anns is None:
            continue

        json_doc = {
            # 'content': document.content,
            'tagme': doc_anns
        }

        filename = os.path.join(outputdir, document.name + '.json')
        json.dump(json_doc, open(filename, 'w'), indent=4, sort_keys=True)

    errors = len([a for a in annotations if a is None])
    if errors > 0:
        logger.warning('{0} documents have been skipped because annotation errors.'.format(errors))
