# The Graph Pipeline

The Graph Pipeline implements a process that will convert and analyze graph theoretic data producing either or both output formatted and data and reports. The data will be taken through a number of standard stages.

The pipeline consists of the main.py file which instantiate a PipelineProcessor.GraphPipelineProcessor class and calls the following pipeline stage methods on it.

- **load.config** a subclass of Implementer.Configurator called GraphConfigurator will read in a YAML configuration file and any command-line overriding parameters and set up a Implemented.Configurated.GraphConfigurated object called config
- **load** a class Implementer.DataLoader.GraphDataLoader will load in the data given in the directory and file in the config object and produce a Implemented.DataLoaded.GraphDataLoaded object containing the data
-  **prepare** calls submethod *filter*    
    - **filter** instantiates a Implementer.Filterer.GraphFilterer object. This takes parameters from the config object and loads a sequence of subobjects to filter the data in GraphDataLoaded in stages. In each stage the filtered data is returned in the GraphDataLoaded object
- **convert** instantiates a Implementer.Converter.GraphConverter object given a parameter in the config object specifying the class, reads in the data from GraphDataLoaded and produces a Implemented.Converted.GraphConverted object
  - This may involve a Implementer.Converter.GraphConverter.GDFConverter and produce a Implemented.Converted.GraphConverted.GDFConverted object
- (optionally) **analyze** which instantiates a Implementer.Analyzer.GraphAnalyzer object which takes as input a GraphConverted object and produces a Implemented.Analyzed.GraphAnalyzed object
- (optionally) **report** which instantiates a Implementer.Reporter.GraphReporter object which takes as input a GraphAnalyzed object and produces a Implemented.Reported.GraphReported object
  - A Implemented.Exportable.GraphExportable object is created and the GraphReported object can be assigned to this 
  - optionally the GraphConverted object may be assigned to the GraphExportable object
- **export** which instantiates a Implementer.Exporter.GraphExporter object which takes as input a GraphExportable object and exports it to a given set of directories

