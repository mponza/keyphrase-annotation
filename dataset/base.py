import os
import json


from utils.configuration import CONFIG


class BaseDataset(object):
    """
    Base class for a keyphrase dataset.
    
    Each subclass rapresents a dataset and
    it has to implement these two functions:
        * _build_document
        * _data_files

    TODO: reduce code redundance in _data_files function in subclasses.
    """


    def _build_document(self, f):
        """
        Builds an object document from a file.
        """
        raise Exception('__build_document function not implemented in BaseDataset abstract class.')


    def _data_files(self, zippath):
        """
        Iterator over proper files of keyphrase_data.zip.
        """
        raise Exception('_data_files function not implemented in BaseDataset abstract class.')



    def __iter__(self):
        """
        Iterates upon documents of the dataset.
        """
        zippath = CONFIG['keyphrase-data']

        for f in self._data_files(zippath):
            yield self._build_document(f)
