import re

TEXT = "We need to future-proof this. Technologically savvy cross-pollination dog and pony show, so corporate synergy execute, but you gotta smoke test your hypothesis at the end of the day. The horse is out of the barn. Drink the Kool-aid. Copy-paste from stack overflow. Clear blue-water UX, so blue money, or identify pain points. Message the intern who's responsible for the ask for this request? Product launch, and onward and upward, productize the deliverables and focus on the bottom line player-coach, yet can you ballpark the cost per unit for me. Can you run this by clearance?"

PATTERN = re.compile(r'(\w+)-(\w+)')

for match in re.finditer(PATTERN, TEXT):
    print(f"match.group(0) is", match.group(0))
    print(f"match.group(1) is", match.group(1))
    print(f"match.group(2) is", match.group(2))
    
    print(match.expand(r"match.expand: first word is \1 and second word is \2."))
    print(f"match.span(0) is", match.span(0))
    print(f"match.re is", match.re, end="\n\n")