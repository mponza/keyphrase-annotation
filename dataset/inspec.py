import os

from base import BaseDataset
from document import Document

from utils.zipping import extract_nested_zipfile


class InspectDataset(BaseDataset):
    """
    Class for managing Inspect dataset.
    """

    def _data_files(self, zippath):
        """
        Iterates over the files in /keyphrase_data/Inspec Hulth.zip.
        """
        duczip = '/keyphrase_data/Inspec Hulth.zip'
        z = extract_nested_zipfile(zippath.rstrip('\/') + duczip)

        for filename in z.namelist():
            if self._valid_file(filename) and filename.endswith('abstr'):
                with z.open(filename) as f:
                    yield f

    def _valid_file(self, filename):
        """
        Returns
        """
        raise Exception('__build_document function not implemented in ICSIDataset abstract class.')


    def _build_document(self, f):
        name = os.path.basename(f.name).split('.')[0].decode('utf-8')
        return Document(name, f.read().decode('utf-8'))


class InspectTrainingDataset(InspectDataset):
    """
    Class for managing Inspect training dataset.
    """

    def _valid_file(self, filename):
        return 'training' in filename


class InspectValidationDataset(InspectDataset):
    """
    Class for managing Inspect validation dataset.
    """

    def _valid_file(self, filename):
        return 'validation' in filename


class InspectTestDataset(InspectDataset):
    """
    Class for managing Inspect test dataset.
    """

    def _valid_file(self, filename):
        return 'test' in filename
