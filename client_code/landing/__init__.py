from ._anvil_designer import landingTemplate
from anvil import *
import anvil.server

class landing(landingTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
  def handle_click(self, event_name, **event_args):
    """Handle navigation clicks"""
    target = event_args.get('element')
    if target and hasattr(target, 'getAttribute'):
      page = target.getAttribute('data-page')
      if page == 'aboutUs':
        get_open_form('aboutUs')
