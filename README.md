Keyphrase Datasets Annotation via TagMe
=======================================

Setting Up
----------

Set up the configuration file in `keyphrase-extraction/configuration.json`:

	{
		"tagme-token": "TagMe authorization token",
		"keyphrase-data": "Path to keyphrase-data.zip"
	}

where the `tagme-token` can be retrieved by following `Installation and setup` section available [here](https://github.com/marcocor/tagme-python).



Installing Dependencies
-----------------------

If you won't install dependencies system-wide use some virtualization tool, like [Virtualenv](https://virtualenv.pypa.io/en/stable/). Then just install dependencies with:

	pip install -r path_to_requirements.txt


Run
----

You can annotate a dataset with:

	python keyphrase-annotation dataset_name output_dir

where `dataset_name` can be:

	* `duc` for the DUC-2001 dataset.
	* `icsi-asr` or `icsi-ht` for ICSI ASR_Output or Human_Transcript datasets, respectively.
	* `inspec-train`, `inspec-val` or `inspec-test` for Inspec training, validation or test datasets, respectively.
	* `nus` for the NUSkeyphraseCorpus dataset.


Output
------

For each document a json file with TagMe annotations will be generated  in the specified `output_dir`. Each json file has the following structure:

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

The `tagme` field contains a list of Wikipedia Entities (identified by `wiki_title`/`wiki_id`) annotated in the input document. For each annotated entity, `annotations` provides information where the corresponding entity has been annotated in the document.

