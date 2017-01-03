import tagme

from logging import getLogger

from utils.configuration import CONFIG

logger = getLogger(__name__)


tagme.GCUBE_TOKEN = CONFIG['tagme-token']


def annotate(document):
    """
    Returns a set of annotations grouped by Wikipedia Title.
    None if errors occur.
    """
    try:
        annotations = tagme.annotate(document.content).annotations
        logger.info('Document {0} correctly annotated!'.format(document.name))

        """
        Group annotations by Wikipedia Title, so for each Wikipedia Entity
        we can see where it has been annotated in the document.

        In detail, grouped_anns will be a LIST of:

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
        """

        grouped_anns = []
        for wiki_title in set([a.entity_title for a in annotations]):

            wiki_annotation = {
                               'wiki_title': wiki_title,
                               'annotations': []
                               }

            for a in [a for a in annotations if a.entity_title == wiki_title]:
                wiki_annotation['wiki_id'] = a.entity_id
                wiki_annotation['annotations'].append(
                    {
                        'begin':    a.begin,
                        'end':      a.end,
                        'score':    a.score,
                        'spot':     a.mention
                    })


            grouped_anns.append(wiki_annotation)            

        return grouped_anns

    except Exception, excp:
        logger.error('Exception while annotating document {0}: {1}'.format(document.name, excp))
        return None
