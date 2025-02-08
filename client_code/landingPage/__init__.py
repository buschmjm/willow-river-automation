from ._anvil_designer import landingPageTemplate
from anvil import *

class landingPage(landingPageTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        """This method is called when the form is shown on the page"""
        # Set the HTML content directly to the HTML component
        self.content_html.html = """
        <div class="landing-content">
            <div class="header landing-header">
                <h1>Willow River Automation Services</h1>
                <h2>Streamlining Workflows, Automating Success.</h2>
            </div>
            <div class="hero">
                <h1>Optimize your business with cutting-edge automation solutions.</h1>
                <p>Discover Our Services!</p>
                <button>Get Started</button>
            </div>
            <!-- ... rest of your HTML content ... -->
        </div>
        """
