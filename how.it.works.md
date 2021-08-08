# How It Works

Each pipeline has the same functionality and structure.

For each pipeline
- there is main script called main.py
  - main.py calls a Pipeline Processor (or Processor) object
  - Processor calls the different stages of the pipeline which can be one or all of
    - load.config
    - load
    - prepare
      - clean
      - filter
    - convert
    - analyze
    - visualize
    - report
    - export

Each of these stages is implemented by a Implementer object which usually produces a Implemented object.
For example, load config is implemented by a ConfigImplementer object and produces a ConfigImplemented object usually called config.

Each stage is a method on the Processor object called inside the main.py script. The stage method in turn calls the Implementer that is appropriate.
The meaning of each Implementer and Implemented object will depend on which pipeline is involved and which stage.

For example, there could be for the graph pipeline and the convert data stage a GDFGraphConverter and GDFConverted Implementer/Implemented pair. Not all pipelines will call all the stage methods and not all stage methods for a particular pipeline Processor will do anything.

The main scripts for each pipeline live in directories called <type>_pipeline for example nlp_pipeline. The objects and classes live in a main module called **pipeline_classes**.
  
## How can these pipelines be used
  
1. One way to use these pipelines is on a dedicated server
  - set up an input and output directory
  - install pip and the requirements.txt file
  - install the pipeline scripts in a dedicated directory 
  - create a configuration file and data file and place these in the input directory
  - run the main.py script

2. Run the pipeline on AWS
  - set up an input and output S3 bucket
  - set up a ECS container with the pip requirements file and the main.py script and pipeline classes module
  - create a configuration file and data file and place in the input bucket
  - install a task to run the ECS container periodically watching the input bucket
  - (optionally) you could use a lambda if you know that main.py will only take at most 15 minutes




