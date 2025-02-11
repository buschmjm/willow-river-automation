from ._anvil_designer import aboutUsTemplate
from anvil import *
import anvil.server

class aboutUs(aboutUsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
  def handle_click(self, event_name, **event_args):
    """Handle navigation clicks"""
    target = event_args.get('element')
    if target and hasattr(target, 'getAttribute'):
      page = target.getAttribute('data-page')
      if page == 'landing':
        get_open_form('landing')
