import os
import json


from utils.configuration import CONFIG


class BaseDataset(object):
    """
    Base class for a dataset.
    
    Each subclass rapresents a dataset and
    it has to implement (*) _build_document and
    (*) _data_files functions.
    """


    def _build_document(self, f):
        """
        Builds an object document from a file.
        """
        raise Exception('__build_document function not implemented in KeyphraseDataset abstract class.')


    def _data_files(self, zippath):
        """
        Iterator over proper files of keyphrase_data.zip.
        """
        raise Exception('_data_files function not implemented in KeyphraseDataset abstract class.')



    def __iter__(self):
        """
        Iterates upon documents of the dataset.
        """
        zippath = CONFIG['keyphrase-data']

        for f in self._data_files(zippath):
            yield self._build_document(f)

