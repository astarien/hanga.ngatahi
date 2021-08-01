# The Paths Pipeline

The Paths Pipeline consists of the main.py file which instantiate a PipelineProcessor.PathsPipelineProcessor class and calls the following pipeline stage methods on it.

- **load_config** a subclass of Implementer.Configurator called PathsConfigurator will read in a YAML configuration file and any command-line overriding parameters and set up a Implemented.Configurated.PathsConfigurated object called config
- **load_data** a class Implementer.DataLoader.PathsDataLoader will load in the data given in the directory and file in the config object and produce a Implemented.DataLoaded.PathsDataLoaded object containing the data
-  **prepare_data** calls submethod *filter_data*    
    - **filter_data** instantiates a Implementer.Filterer.PathsFilterer object. This takes parameters from the config object and loads a sequence of subobjects to filter the data in GraphDataLoaded in stages. In each stage the filtered data is returned in the PathsDataLoaded object
- **convert_data** instantiates a Implementer.Converter.GraphConverter object given a parameter in the config object specifying the class, reads in the data from PathsDataLoaded and produces a Implemented.Converted.PathsConverted object
  - This may involve a Implementer.Converter.PathsConverter.JSONConverter and produce a Implemented.Converted.PathsConverted.SankeyConverted object
- (optionally) **analyze_data** which instantiates a Implementer.Analyzer.PathsAnalyzer object which takes as input a PathsConverted object and produces a Implemented.Analyzed.PathsAnalyzed object
- (optionally) **build_report** which instantiates a Implementer.Reporter.PathsReporter object which takes as input a PathsAnalyzed object and produces a Implemented.Reported.PathsReported object
  - A Implementable.Exportable.PathsExportable object is created and the PathsReported object can be assigned to this 
  - optionally the PathsConverted object may be assigned to the PathsExportable object
- **export_data** which instantiates a Implementer.Exporter.PathsExporter object which takes as input a PathsExportable object and exports it to a given set of directories




