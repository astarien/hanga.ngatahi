# How It Works

Each pipeline has the same functionality and structure.

For each pipeline
- there is main script called main.py
  - main.py calls a Pipeline Processor (or Processor) object
  - Processor calls the different stages of the pipeline which can be one or all of
    - load config
    - load data
    - prepare data
      - clean data
      - filter data
    - convert data
    - analyze data
    - build visualizations
    - build reports
    - export data

Each of these stages is implemented by a Implementer object which usually produces a Implemented object.
For example, load config is implemented by a ConfigImplementer object and produces a ConfigImplemented object usually called config.

Each stage is a method on the Processor object called inside the main.py script. The stage method in turn calls the Implementer that is appropriate.
The meaning of each Implementer and Implemented object will depend on which pipeline is involved and which stage.

For example, there could be for the graph pipeline and the convert data stage a GDFGraphConverter and GDFConverted Implementer/Implemented pair. Not all pipelines will call all the stage methods and not all stage methods for a particular pipeline Processor will do anything.

The main scripts for each pipeline live in directories called <type>_pipeline for example nlp_pipeline. The objects and classes live in a main module called classes.
  


