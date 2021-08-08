#
import implementers, implemented
import implementables.exportables as exportables

def load.config():
  
  config = implemented.ConfigImplemented()
  
  return config

def load(config):
  
  data = implementers.DataLoader(config)
  
  return data

def clean(data, config):
  
  return data

def filter(data, config):
  
  return data

def prepare(data, config):
  
  data = clean(data, config)
  data = filter(data, config)
  
  return data

def convert(exported, config):
  
  converteddata = implementers.DataConverter(exported.get(0))
  exported.add(converteddata)
  
  return exported

def report(exported, config):
  
  report = implementers.Reporter(exported.get(0), exported.get(1))
  exported.add(report)
  
  return exported

def export(exported, config):
  
  for i in range(exported.num_items()):
    exportitem = exported.get(i)
    # do export
    
  return
  
