import tagme

from itertools import combinations
from utils.configuration import CONFIG
from logging import getLogger

logger = getLogger(__name__)

tagme.GCUBE_TOKEN = CONFIG['tagme-token']

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()



def entity_pairs_relatedness(annotated_document):
    """
    The annotated_document is a dictionary:

    {
        'tagme':
            {
                'wiki_title': str,
                'wiki_id': str,
                'annotations':
                    [
                        {
                            'begin':    int,
                            'end':      int,
                            'score':    float,
                            'spot':     str
                        }
                    ]
            }
    }

    And this function returns the relatedness annotations, namely:
    
    [
        {
            'src_wiki_id': int,
            'dst_wiki_id': int,
            'score': float
        }
    ]

    where 'score' is the value of the Milne-Witten relatedness function.
    """
    
    # rho_treshold = lambda annotations: any(a['score'] >= 0.0 for a in annotations)

    entities = [a['wiki_id'] for a in annotated_document['tagme']]

    logger.info('{0}'.format(len(entities)))

    if len(entities) <= 1:
        return []

    max_retries = 3
    for i in xrange(1, max_retries + 1):
        try:
            logger.info('{0} entities'.format(len(entities)))
            entity_pairs = list(combinations(entities, 2))

            related_annotations = tagme.relatedness_wid(entity_pairs)

            relatedness = []
            for entity_pair, rel_score in related_annotations:

                src = entity_pair[0]
                dst = entity_pair[1]

                relatedness.append({
                    'src_wiki_id': src,
                    'dst_wiki_id': dst,
                    'score': rel_score}
                    )

            logger.info('Computed {0} relatedness from one single documents'.format(len(entity_pairs)))
            return relatedness

        except Exception, exc:

            if i == max_retries:
                raise Exception('TagMe Relatedness error.\
                                Maximum attempts reached. {0}'.format(exc))
                return None

            else:
                logger.warning('Errors while computing relatedness \
                                {0} attempt. Error: {1}'.format(i, exc))