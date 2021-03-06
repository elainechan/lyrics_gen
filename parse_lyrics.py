import random
import re
import collections
from nltk.corpus import stopwords

text = """My song is love
My song is love, unknown
And it goes up
You don't have to be alone
My heavy heart
Looks like it's made of stone
But it's so hard to see, clearly
You don't have to be on your own
You don't have to be on your own
And I'm not gonna take it back
Oh I'm not gonna say I don't mean that
You're the target that I'm aiming at
And I'm not singing on my own
That bitter breathe
That bitter breathe has blown
Left me on fire, for you, clearly
Taken everything and gone
It’s taken everything I own
But I'm not gonna take it back
I’m not gonna say I don’t mean that
You're the target that I'm aiming at
And I'm nothing on my own
Got to get that message home
I'm not gonna stand and wait
Not gonna leave it until it's much too late
On a platform I'm gonna stand and say
Oh I'm nothing on my own
Till that bitter breathe has blown
My song is love, Is love uknown
And I’ve got to get that message home"""

print(text)

def lows(word):
    return word.lower()

words = list(map(lows, re.findall(r"[\w']+", text) ))

def fil(word):
    stops = ['and', 'or', 'but', 'that', 'this']
    return word not in stops

filtered_words = list(filter(fil, words))

freq = collections.Counter(words)
filtered_freq = collections.Counter(filtered_words)

print(freq)
print("---")
print(filtered_freq)