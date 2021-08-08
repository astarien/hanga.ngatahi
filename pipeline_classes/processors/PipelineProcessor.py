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

def convert(data, config):
  
  converteddata = implementers.DataConverter(data)
  return converteddata

def report(data, converteddata, config):
  
  report = implementers.Reporter(data, converteddata)
  return report

def export(exported, config):
  
  for i in range(exported.num_items()):
    exportitem = exported.get(i)
    # do export
    
  return
  
