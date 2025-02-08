from ._anvil_designer import landingPageTemplate
from anvil import *


class landingPage(landingPageTemplate):
  def __init__(self, **properties):
        self.init_components(**properties)

        # Set background image dynamically
        self.set_background_image()

  def set_background_image(self):
        # Apply background image from the assets folder
        self.role = "background"
        self.style["backgroundImage"] = "url('_/theme/laptop-593673.jpg')"
        self.style["backgroundSize"] = "cover"
        self.style["backgroundPosition"] = "center"
        self.style["backgroundRepeat"] = "no-repeat"
