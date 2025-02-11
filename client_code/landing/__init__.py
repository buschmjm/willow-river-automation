from ._anvil_designer import landingTemplate
from anvil import *
import anvil.server

class landing(landingTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
  def handle_click(self, **event_args):
    """Handle navigation clicks"""
    if 'data-page' in event_args['event_target'].attrs:
      page = event_args['event_target'].attrs['data-page']
      if page == 'aboutUs':
        open_form('aboutUs')
