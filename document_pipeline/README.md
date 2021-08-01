# The Document Pipeline

The Document Pipeline consists of the main.py file which instantiate a PipelineProcessor.DocumentPipelineProcessor class and calls the following pipeline stage methods on it.

- **load_config** a subclass of Implementer.Configurator called DocumentConfigurator will read in a YAML configuration file and any command-line overriding parameters and set up a Implemented.Configurated.DocumentConfigurated object called config
- **load_data** a class Implementer.DataLoader.DocumentDataLoader will load in the data given in the directory and file in the config object and produce a Implemented.DataLoaded.DocumentDataLoaded object containing the data
    - This may use a subclass of DocumentDataLoader such as JSONDataLoader or NoSQLDataLoader which would read the data in in JSON format or connect to a NoSQL database using a class such as NoSQLDataLoader.MongoDBDataLoader
    - It will produce DataLoaded object such as JSONDataLoaded or NoSQLDataLoaded
-  **prepare_data** calls submethod *filter_data*    
    - **filter_data** instantiates a Implementer.Filterer.DocumentFilterer object. This takes parameters from the config object and loads a sequence of subobjects to filter the data in DocumentDataLoaded in stages. In each stage the filtered data is returned in the DocumentDataLoaded object
        - Behind the scenes there may be a DocumentFilterer.NoSQLFilterer.MongoDBFilterer object 
- **convert_data** instantiates a Implementer.Converter.DocumentConverter object given a parameter in the config object specifying the class, reads in the data from GraphDataLoaded and produces a Implemented.Converted.DocumentConverted object
    - Behind the scenes there may be a DocumentConverter.NoSQLConverter.MongoDBConverter object that produces a DocumentConverted.TabularConverted object wrapping data in tabular format
  - (optionally) **analyze_data** which instantiates a Implementer.Analyzer.DocumentAnalyzer object which takes as input a DocumentConverted object and produces a Implemented.Analyzed.DocumentAnalyzed object
- (optionally) **build_report** which instantiates a Implementer.Reporter.DocumentReporter object which takes as input a DocumentAnalyzed object and produces a Implemented.Reported.DocumentReported object
  - A Implementable.Exportable.DocumentExportable object is created and the DocumentReported object can be assigned to this 
  - optionally the DocumentConverted object may be assigned to the DocumentExportable object
- **export_data** which instantiates a Implementer.Exporter.DocumentExporter object which takes as input a DocumentExportable object and exports it to a given set of directories



