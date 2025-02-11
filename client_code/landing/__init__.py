from ._anvil_designer import landingTemplate
from anvil import *
import anvil.server

class landing(landingTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
  def handle_click(self, **event_args):
    """Handle navigation clicks"""
    if hasattr(event_args['sender'], 'tag'):
      clicked = event_args['sender']
      if clicked.tag.name == 'A' and clicked.get_attribute('data-page') == 'aboutUs':
        open_form('aboutUs')
