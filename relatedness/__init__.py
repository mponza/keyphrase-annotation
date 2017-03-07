import os
import json
import progressbar

from logging import getLogger
from multiprocessing import Pool
from gensim.utils import chunkize

from relate import entity_pairs_relatedness


logger = getLogger(__name__)



def tagme_relatedness(dataset_dir, output_dir):
    """
    Enhances each document of documents_dir with the relatedness between its
    entity pairs and saves them into a json file in output_dir.
    """
    documents = [name for name in os.listdir(dataset_dir) if name.endswith('json')]
    logger.info('{0} documents read from {1}'.format(len(documents), dataset_dir))


    # File reading
    tagme_docs = []
    output_filenames = []
    for doc_name in documents:

        input_filename = os.path.join(dataset_dir, doc_name)
        with open(input_filename, 'r') as f:
            tagme_docs.append(json.load(f))

        outfilename = os.path.join(output_dir, doc_name)
        output_filenames.append(outfilename)


    # Parallel relatedness annotation
    errors = 0
    i = 0
    pool = Pool(8)
    for chunk_docs in chunkize(tagme_docs, 8):
        relates = pool.map(entity_pairs_relatedness, chunk_docs)

        for j in range(i, min(i + 8, len(tagme_docs))):
            annotated_document = tagme_docs[j]
            annotated_document = tagme_docs[j]

            annotated_document['relatedness'] = relates[j % 8]

            outfilename = output_filenames[j]

            if annotated_document['relatedness'] is None:
                logger.error('Relatedness errors for document {0}. Skipped.'
                                .format(input_filename))
                errors += 1

            outdir = os.path.dirname(outfilename)
            if not os.path.exists(outdir):
                os.makedirs(outdir)

            with open(outfilename, 'w') as f:
               json.dump(annotated_document, f, indent=4, sort_keys=True)

        i += len(chunk_docs)
        logger.info('Entity Pair Relatedness computed for {0} documents.'
                    .format(i))


    # Relatedness annotation without Pool

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

