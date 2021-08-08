#
import implementers, implemented
import implementables.exportables as exportable

def load.config():
  
  config = implemented.ConfigImplemented()
  
  return config

def load(config):
  
  data = implementers.DataLoader(config)
  
  return data

def clean(data):
  
  return data

def filter(data):
  
  return data

def prepare(data):
  
  data = clean(data)
  data = filter(data)
  
  return data

def convert(data):
  
  converteddata = implementers.DataConverter(data)
  exported = exportables.Exportable()
  exported.add(converteddata)
  
  return exported

def report(data, exported):
  
  report = implementers.Reporter(data, exported.converted())
  exported.add(report)
  
  return exported

def export(exported):
  
  return
  
