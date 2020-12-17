from ezprez.core import *
from ezprez.components import *

# Setup your Slide's (Note they don't need to be added anywhere by default)
Slide("Hello world", "This is a basic slide")
Slide("Hello world", "This is a basic slide that's black", background="black")
Slide("You can also use components", "Like Icons", Icon("fa-heart",color="red"))

# Automatically includes the above slides
prez = Presentation("This is a demo", "To show off exprez", "https://example.com")
prez.export(".", "Presentation", force=True) # Export files to ./Presentation