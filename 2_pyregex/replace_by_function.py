import re

def reverse_caps(match):
    reversed = match.group(0)[::-1]
    all_caps = reversed.upper()
    return all_caps

def insert_hyphens(match):
    replacement_string = ""
    for letter in match.group(0):
        replacement_string += letter.upper()
        replacement_string += "-"
    replacement_string = replacement_string.strip("-")
    return replacement_string

def lowini(match):
    replacement_string = ""
    for letter in match.group(0):
        replacement_string = letter.upper()
    return replacement_string
    
TEXT = "I know somebody who can do this for a reasonable cost. Can you make the font bigger? Thanks for taking the time to make the website, but I already made it in WIX. I know you've made thirty iterations but can we go back to the first one that was the best version, yet can you make pink a little more pinkish? Can you make it faster? But I was wondering if my cat could be placed over the logo in the flyer. You are lucky to even be doing this. For us, the animation does not work, when I print the page could you move it a tad to the left? That's great, but can you make it work for Internet Explorer 2 please, so make the font bigger. Remember, everything is the same or better, so can you remove my double chin on my business card photo? I don't like the way it looks. Could you do an actual logo instead of a font, so can you use a high definition screenshot, or is this the best we can do give us a complimentary logo along with the website? I love it, but can you invert all colors? We are a non-profit organization. Our budget is limited. We can try your approach, but can you change everything afterwards?"

PATTERN = re.compile(r"\b[A-Z][\w\-']+\b")

# replacement, num = re.subn(PATTERN, reverse_caps, TEXT) # num is number of replacements made
replacement = re.sub(PATTERN, lowini, TEXT)

print(replacement)