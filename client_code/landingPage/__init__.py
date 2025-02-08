from ._anvil_designer import landingPageTemplate
from anvil import *

class landingPage(landingPageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Load the external HTML file into the HTML component
        with open("_/theme/staticLanding.html", 'r') as f:
            html_string = f.read()
        self.html = html_string
