from collections import Counter
from typing import Optional

# def build_words_from_characters(characters: str, word_length: int) -> list[str]:
#     """Return dictionary words constructible from the supplied characters."""
#     if not characters.isalpha() or word_length < 1:
#         raise ValueError("Use only letters and a positive word length.")
#     available = Counter(characters.casefold())
#     with open(r"C:\Users\samwa\OneDrive - Metrolinx\!P\!Projects\!!DATA\English Words\words.txt", encoding="utf-8") as dictionary:
#     #with open(r"C:\Users\samwa\OneDrive - Metrolinx\P\!Projects\!!DATA\English Words\words.txt", encoding="utf-8") as dictionary:
#         return sorted({
#             word for line in dictionary 
#             if len(word := line.strip().casefold()) == word_length 
#             and word.isalpha() 
#             and not (Counter(word) - available)
#             })

def build_words_from_characters_ex(characters: str, word_length: int, char_already_included: Optional [dict[int, str]] = None) -> list[str]:
    """Return constructible dictionary words matching zero-based fixed positions."""
    if not characters.isalpha() or word_length < 1: raise ValueError("Use only letters and a positive word length.")
    fixed = {position: character.casefold() for position, character in (char_already_included or {}).items()}
    if any(not isinstance(position, int) or position not in range(word_length) or len(character) != 1 or not character.isalpha() for position, character in fixed.items()): raise ValueError(f"Indexes must be from 0 to {word_length - 1}, with one letter per index.")
    available = Counter(characters.casefold())
    with open(r"C:\Users\samwa\OneDrive - Metrolinx\!P\!Projects\!!DATA\English Words\words.txt", encoding="utf-8") as dictionary: 
        return sorted({
            word for line in dictionary 
            if len(word := line.strip().casefold()) == word_length 
            and word.isalpha() 
            and not (Counter(word) - available) 
            and all(word[position] == character for position, character in fixed.items())
            })

print(build_words_from_characters_ex("airnb", 4, {2:'a'}))
# print(build_words_from_characters_ex("acre", 4))
# print(build_words_from_characters_ex("acre", 4,{2:'e'}))
# print(build_words_from_characters_ex("acre", 4,{0:'a'}))
# print(build_words_from_characters_ex("acre", 4,{0:'a' , 2:'e'}))
# #print(build_words_from_characters("GTNIH", 4))