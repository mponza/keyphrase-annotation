import os
import json
import progressbar

from logging import getLogger
from multiprocessing import Pool

from relate import entity_pairs_relatedness


logger = getLogger(__name__)



def tagme_relatedness(dataset_dir, output_dir):
    """
    Enhances each document of documents_dir with the relatedness between its
    entity pairs and saves them into a json file in output_dir.
    """
    documents = [name for name in os.listdir(dataset_dir) if name.endswith('json')]
    logger.info('{0} documents read from {1}'.format(len(documents), dataset_dir))


    tagme_docs = []
    output_filenames = []
    for doc_name in documents:

        input_filename = os.path.join(dataset_dir, doc_name)
        with open(input_filename, 'r') as f:
            tagme_docs.append(json.load(f))

        outfilename = os.path.join(output_dir, doc_name)
        output_filenames.append(outfilename)

    relates = Pool(8).map(entity_pairs_relatedness, tagme_docs)

    errors = 0
    for i in range(0, len(relates)):
        annotated_document = tagme_docs[i]
        annotated_document['relatedness'] = relates[i]
        outfilename = output_filenames[i]

        if annotated_document['relatedness'] is None:
            logger.error('Relatedness errors for document {0}. Skipped.'
                            .format(input_filename))
            errors += 1

        outdir = os.path.dirname(outfilename)
        if not os.path.exists(outdir):
            os.makedirs(outdir)

        with open(outfilename, 'w') as f:
           json.dump(annotated_document, f, indent=4, sort_keys=True)



    # Without Pool

    # errors = 0
    # bar = progressbar.ProgressBar()
    # for doc_name in bar(documents):
    # 	# Absolute filenames
    # 	input_filename = os.path.join(dataset_dir, doc_name)
    # 	output_filename = os.path.join(output_dir, doc_name)

    #     # Loads and annotate with entity pair relatedness.
    # 	annotated_document = json.load(open(input_filename, 'r'))
    #     relatedness = entity_pairs_relatedness(annotated_document)

    #     if relatedness is None:
    #         logger.error('Relatedness errors for document {0}. Skipped.'.format(input_filename))
    #         errors += 1
    #         continue

    # 	annotated_document['relatedness'] = relatedness


    #     outdir = os.path.dirname(output_filename)
    #     if not os.path.exists(outdir):
    #         logger.warn('Creating directory {0}'.format(outdir))
    #         os.makedirs(outdir)

    #     with open(output_filename, 'w') as f:
    # 	   json.dump(annotated_document, f, indent=4, sort_keys=True)


    if errors > 0:
        logger.warning('{0} documents have been skipped because annotation errors.'.format(errors))

    logger.info('Relatedness Computation for directory {0} ended.'.format(dataset_dir))

