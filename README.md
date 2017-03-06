Keyphrase Dataset Annotation via TagMe
=======================================

Setting Up
----------

Set up a json file in `keyphrase-annotation/configuration.json`:

	{
		"tagme-token": "TagMe authorization token",
		"keyphrase-data": "Path to keyphrase_data.zip"
	}

where the `tagme-token` can be retrieved by following `Installation and setup` section available [here](https://github.com/marcocor/tagme-python).



Installing Dependencies
-----------------------

If you won't install dependencies system-wide use some virtualization tool, like [Virtualenv](https://virtualenv.pypa.io/en/stable/). Then just install dependencies with:

	pip install -r keyphrase-annotation/requirements.txt


Running TagMe Annotator
-----------------------

You can annotate a single dataset with:

	python keyphrase-annotation annotate dataset_name annotation_dir

where `dataset_name` can be:

 * `duc` for the DUC-2001 dataset.
 * `icsi-asr` or `icsi-ht` for ICSI ASR_Output or Human_Transcript datasets, respectively.
 * `inspec-train`, `inspec-val` or `inspec-test` for Inspec training, validation or test datasets, respectively.
 * `nus` for the NUSkeyphraseCorpus dataset.

You can also annotate all datasets at once by typing:

	python keyphrase-annotation annotate_all annotation_dir

and the annotations for each dataset will be saved in the corresponding folder inside `annotation_dir` (for example, the annotations of the DUC-2001 dataset will be saved into `annotation_dir/duc`).


For each document a json file with TagMe annotations will be generated in the specified folder. Each json file has the following structure:

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

The `tagme` field contains a list of Wikipedia Entities (each entity is uniquely identified by its `wiki_title`/`wiki_id`) annotated in the input document. For each annotated entity, `annotations` provides information where the corresponding entity has been annotated in the document. `score` is the TagMe  coherence score between that annotation and the others in the surrounding text.



Running TagMe Relatedness
-------------------------

The datasets annotated with TagMe can be futher enhanced with the relatedness score of entity pairs:

	python keyphrase-annotation relatedness annotation_dir relate_dir

where `annotation_dir` is the directory previously used to store the TagMe annotations and `relate_dir` is the new output directory.

The previous annotations will be preserved and enhanced with the relatedness scores between all pairs of entities contained in the corresponding document:

	{
		"tagme": see tagme field above

		"relatedness":
			[
				{
					"src_wiki_id":	int,
					"dst_wiki_id":	int,
					"score":		float
				}
			]
	}

where `score` is thre Milne&Witten relatedness score between `src_wiki_id` and `dst_wiki_id`.