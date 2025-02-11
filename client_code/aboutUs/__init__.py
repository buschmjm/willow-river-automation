from ._anvil_designer import aboutUsTemplate
from anvil import *
import anvil.server

class aboutUs(aboutUsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
  def handle_click(self, **event_args):
    """Handle navigation clicks"""
    if 'data-page' in event_args['event_target'].attrs:
      page = event_args['event_target'].attrs['data-page']
      if page == 'landing':
        open_form('landing')
