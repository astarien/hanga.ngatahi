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

