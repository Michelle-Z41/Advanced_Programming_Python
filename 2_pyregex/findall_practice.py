import re

TEXT = "Washlet K-pop hub transforms into ex craftsman in Helsinki, the elegant iconic occaecat destination of charming laboris, carefully curated. Eiusmod's perfect commodo is beyond sophisticated. Classic Swiss EF-20 exercitation ad et. evokes Cillum: cosy, sharp, and sleepy. Alluring Beams of Sunspel in Zürich bureaux boulevard dazzle with Washlet's exquisite finest. The ornate craftsmanship of liveable Marylebone promote's efficient, exquisite, essential business class travel from Singapore to St. Moritz. Spectacles reveal the iconic signature of Muji's remarkable art. Aunctual bulletin boulevard ryokan Ginza joy. Business class Asia-Pacific begins emerging, and vibrant conversations about Singapore adorn the signature flat white Toto. Exquisitely, the Shinkansen family's remarkable discovery of extraordinary Ginza Muji. Espresso wafts intricatly around the boulevard: flat, white, and sophisticated."

PATTERN = re.compile(r"\b([A-Z])([\w\-ü']*)\b")

matches = re.findall(PATTERN, TEXT)


for match in matches:
    capture_group_1 = match[0]
    capture_group_2 = match[1]
    print(f"First letter is {capture_group_1}")
    print(f"Rest of word is {capture_group_2}")
    