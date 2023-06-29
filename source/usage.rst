***************************
How to create/update CLU
***************************

Generically, there are four main steps in creating and/or updatign the CLU model for TOBi voice:

* Create utterances for Intents
* Create entities
* Import, train, deploy CLU model 
* Validate CLU model on blindset data

Below, we go through each of the steps in detail.

=====================
Intents
=====================

In Composer (the tool used to build dialog journeys), there is a list of pre-defined intents (usually one per journey) that are needed for inclusion in the CLU model.

.. figure:: /figures/composer_intents.png
    :width: 600
    :align: center
    :alt: The location of the intents defined in Composer and that need an intent in CLU model.
    
    The location of the intents defined in Composer and that need an intent in CLU model. All but the Unknown intent should be included in CLU.


Once we get the full list of intents to create and/or update, we should start collecting utterances (simple sentences that should map to a specific intent). 
The utterances should be added to the file at :code:`data\raw\gpt-agumentation\gpt_data.txt`, using the following structure:

.. code-block::

    IDNN_IE_intentName1
    utterance 1
    utterance 2
    ...
    IDNN_IE_intentName2
    utterance 1
    ...


Once the utterance collection is finished, we run the :code:`data\raw\gpt-agumentation\create_dataframe.py` script to convert the file above into a csv file. This will be the file to use for populating the CLU data.

Our preferred method is to use `chatGPT`_ to create these utterances. An example of a prompt can be found below:

.. code-block::
    
    You are in the context of calling a chatbot operator for a telecom company. Can you tell me 10 different ways of saying
    "I want to check my balance"? Use a conversational style.

.. note::
    In principle, any file with two columns (one for the utterances, one for the intents) can be used to upload to the CLU model.
    However, for ease of use with `chatGPT`_ responses, the proposed format above works better, as it allows a simple copy/paste operation to keep adding to the file, on an intent per intent basis.

=====================
Entities
=====================

For creating entities, we need to go through each journey im Composer and figure out which information is requested throughout. Usually this entails going through every user prompt and respective ``Switch Case``.


.. figure:: /figures/composer_entities.png
    :width: 600
    :align: center
    :alt: The search for entites in a journey.

    The search for entities in the journey can be split in 4 different steps: (1) select the dialog to study and click *BeginDialog*; (2) On the middle panel, indentify the user input; (3) Click the *Branch Switch* box; (4) collect the different values that are expected from the user. These values should map to one list in CLU for the same entity name.

For each possible answer of a ``Switch Case``, one needs to define an entity of the ``list`` type (for more information on component types, please refer to `CLU documentation <https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/conversational-language-understanding/concepts/entity-components>`_). Once we collect this information, we should map it into the excel file at ``data\raw\Entities.xlsx``. IT should look something like:

.. csv-table:: Entities
    :header: "journey",	"category", "options",	"list",	"prebuilts", "regex"
    :delim: ;

        GLOBAL;global_truefalse;;;Choice.Boolean;
        GLOBAL;global_confirmation;yes, no;Yes, yes, sure, yeah;;
        ;;;No, no, nope, nah;;;
        ID02_IE_manageAddOns;manageAddOns_service;help, purchase, cancel;Help, help;;
        ;;;Purchase, buy, Buy, purchase;;
        ;;;Cancel, cancel, terminate;;
        ID02_IE_manageAddOns;manageAddOns_options;app, free text;App, app, application, myvodafone;;
        ;;;Free Text, text, Text, SMS, message;;
        ID13_IE_appProblems;appProblems_issue;credit balance, topup, something else;Credit balance, credit, balance;;
        ;;;Top Up, topup, top up;;
        ;;;Something else, other;;

Where each column represents:

* **journey** - The name of the journey/dialog the entity is associated with. For general entities use ``GLOBAL``.
* **category** - The name of the entity (this will be used in composer to access the value guessed by CLU). It should follow the format ``journeyName_entityDescription``.
* **options** - For readability purposes, this shoul include all options of the ``Switch Case`` associated with the entity.
* **list** - This should include a comma-separated list of all the words that map into a specific keyword. It should follow the format ``keyword, word1, word2, ...``
* **prebuilts** - One of the keywords supported by CLU (see `supported cases <https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/conversational-language-understanding/prebuilt-component-reference>`_ [#f1]_).
* **regex** - regular expression to be used in matching. the format should be ``key, regular_expression``.

The current pipeline will then take care of converting the information on this excel file into an appropriate format to upload to Microsoft CLU.

=====================
CLU update
=====================

Run the notebook at ``notebooks\CLU_pipeline.ipynb``. You'll find there specific notes annotated in Markdown.


=====================
Validation testing
=====================

Run the notebook at ``notebooks\CLU_ValidationTests.ipynb``. You'll find there specific notes annotated in Markdown.



.. _chatGPT: https://chat.openai.com/chat

.. rubric:: Footnotes

.. [#f1] This list is not up-to-date. You can check the newer options from CLU Language studio, after selecting one entity in the *Schema Definition* tab, and selectingone entity and try to *Add new prebuilt*.