Keyphrase Dataset Annotation via TagMe
=======================================

Setting Up
----------

Set up a json file in `keyphrase-extraction/configuration.json`:

	{
		"tagme-token": "TagMe authorization token",
		"keyphrase-data": "Path to keyphrase-data.zip"
	}

where the `tagme-token` can be retrieved by following `Installation and setup` section available [here](https://github.com/marcocor/tagme-python).



Installing Dependencies
-----------------------

If you won't install dependencies system-wide use some virtualization tool, like [Virtualenv](https://virtualenv.pypa.io/en/stable/). Then just install dependencies with:

	pip install -r path_to_requirements.txt


Running
-------

You can annotate a single dataset with:

	python keyphrase-annotation annotate dataset_name output_dir

where `dataset_name` can be:

 * `duc` for the DUC-2001 dataset.
 * `icsi-asr` or `icsi-ht` for ICSI ASR_Output or Human_Transcript datasets, respectively.
 * `inspec-train`, `inspec-val` or `inspec-test` for Inspec training, validation or test datasets, respectively.
 * `nus` for the NUSkeyphraseCorpus dataset.

You can also annotate all datasets by typing:

	python keyphrase-annotation annotate_all output_dir

and the annotations for each dataset will be saved the corresponding in folder into `output_dir` (example: the annotations of the DUC-2001 dataset will be saved into `output_dir/duc`).


Output
------

For each document a json file with TagMe annotations will be generated  in the specified folder. Each json file has the following structure:

	{
		"tagme":
			[
				{
	                "wiki_title": str,
	                "wiki_id": str,
	                "annotations":
	                    [
	                        {
	                            "begin":    int,
	                            "end":      int,
	                            "score":    float,
	                            "spot":     str
	                        }
	                    ]
	            }
	        ]
	}

The `tagme` field contains a list of Wikipedia Entities (each entity is uniquely identified by its `wiki_title`/`wiki_id`) annotated in the input document. For each annotated entity, `annotations` provides information where the corresponding entity has been annotated in the document.
