import os

from base import BaseDataset
from document import Document

from utils.zipping import extract_nested_zipfile


class NUSDataset(BaseDataset):
    """
    Class for managing NUSkeyphraseCorpus dataset.
    """

	def _data_files(self, zippath):
        """
        Iterates over the files in /keyphrase_data/NUSkeyphraseCorpus.zip.
        """
        duczip = '/keyphrase_data/NUSkeyphraseCorpus.zip'
        z = extract_nested_zipfile(zippath.rstrip('\/') + duczip)

        for filename in z.namelist():
            if filename.endswith('.txt'):
                with z.open(filename) as f:
                    yield f

    
    def _build_document(self, f):
        name = os.path.basename(f.name).split('.')[0].decode('utf-8')
        return Document(name, f.read().decode('utf-8'))


