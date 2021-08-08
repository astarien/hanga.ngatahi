# main script for pipeline

import processors
import implementeds
import implementables.exportables as exportables

if __name__ == "__main__":
  
  processor = processors.NLPProcessor()
  
  # Stage 1 - load the configuration parameters
  config = processor.load.config()
  
  # Stage 2 - load the data
  data = processor.load(config)
  
  # Stage 3 - prepare the data given the config - so clean and filter
  data = processor.prepare(data, config)
  
  # set up the exported object
  exported = exportables.NLPExportable()
  exported.add(data)
  
  # Stage 4 - convert the data (optional)
  if config.do_convert():
    exported = processor.convert(exported, config)
  
  # Stage 5 - build the report
  exported = processor.report(exported, config)
  
  # Stage 6 - do the export
  processor.export(exported, config)
