import re
import linkGrabber

links = linkGrabber.Links("https://devx.work")
#gb = links.find(limit=10, duplicates= False, pretty=True)
gb = links.find(pretty=True)


print(gb)