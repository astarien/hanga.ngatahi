# The NLP Pipeline

The NLP pipeline implements a process for using software to process unstructured and textual data through a number of standard stages using Natural Language Processing.

The pipeline consists of the main.py file which instantiate a PipelineProcessor.NLPProcessor class and calls the following pipeline stage methods on it.

- **load.config** a subclass of Implementer.Configurator called NLPConfigurator will read in a YAML configuration file and any command-line overriding parameters and set up a Implementable.Configurated.NLPConfigurated object called config
- **load** a class Implementer.DataLoader.NLPDataLoader will load in the data given in the directory and file in the config object and produce a Implemented.DataLoaded.NLPDataLoaded object containing the data
-  **prepare** calls submethods *clean* and *filter*
    - **clean** instantiates a Implementer.Cleaner.NLPCleaner object which cleans the data in NLPDataLoaded given a text field and sets the content of NLPDataLoaded to the cleaned data
    - **filter** instantiates a Implementer.Filterer.NLPFilterer object. This takes parameters from the config object and loads a sequence of subobjects to filter the data in NLPDataLoaded in stages. In each stage the filtered data is returned in the NLPDataLoaded object
- **convert** instantiates a Implementer.Converter.NLPCOnverter object given a parameter in the config object specifying the class, reads in the data from NLPDataLoaded and produces a Implemented.Converted.NLPConverted object
  - This may involve a Implementer.Converter.NLPConverter.GensimNMFModelConverter and produce a Implemented.Converted.NLPConverted.GensimNMFConverted object
- **report** which instantiates a Implementer.Reporter.NLPReporter object which takes as input a NLPConverted object and produces a Implemented.Reported.NLPReported object
  - A Implementable.Exportable.NLPExportable object is created and the NLPReported object is assigned to this 
  - optionally the NLPDataLoaded or the NLPCOnverted objects may be assigned to the NLPExportable object
- **export** which instantiates a Implementer.Exporter.NLPExporter object which takes as input a NLPExportable object and exports it to a given set of directories


