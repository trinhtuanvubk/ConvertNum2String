from phonemizer import phonemize

# line1 = 'long'
# line2 = 'lo'
# text = [line1, line2]

# # Do this:
# phonemized = phonemize(text)
# # print(phonemized)
# # Not this:
# # phonemized = [phonemize(line) for line in text]

# # An alternative is to directly instanciate the backend and to call the
# # phonemize function from it:

# from phonemizer.backend import EspeakBackend
# backend = EspeakBackend('vi')
# phonemized = [backend.phonemize(line) for line in text]
# print(phonemized[0])
# print(phonemized[1])



# def to_phoneme(text, lang='vi'):
#     phonemes = phonemize(text,
#                          language=lang,
#                          backend='espeak',
#                          strip=True,
#                          preserve_punctuation=True,
#                          with_stress=False,
#                          njobs=1,
#                          punctuation_marks=';:,.!?¡¿—-…"«»“”()',
#                          language_switch='remove-flags')
#     return phonemes

# print(to_phoneme("long long long long lo lo lo"))
def to_phoneme(text, lang='vi'):
    phonemes = phonemize(text,
                         language=lang,
                         backend='espeak',
                         strip=True,
                         preserve_punctuation=True,
                         with_stress=False,
                         njobs=1,
                         punctuation_marks=';:,.!?¡¿—-…"«»“”()',
                         language_switch='remove-flags')
    return phonemes

text = 'long long lo lo long lo'
print(to_phoneme(text))