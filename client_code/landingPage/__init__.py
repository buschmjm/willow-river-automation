from ._anvil_designer import landingPageTemplate
from anvil import *

class landingPage(landingPageTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        # Set background image dynamically
        self.set_background_image()

    def set_background_image(self):
        # Apply background image to the MAIN FORM
        self.role = "background"

        # Apply background styling to a specific panel (e.g., `column_panel_1`)
        self.outlined_card_1.style["backgroundImage"] = "url('_/theme/laptop-593673.jpg')"
        self.outlined_card_1.style["backgroundSize"] = "cover"
        self.outlined_card_1.style["backgroundPosition"] = "center"
        self.outlined_card_1.style["backgroundRepeat"] = "no-repeat"
