# Project idea: Extracting information about the news articles.
# Developed by: Meqdad Darweesh

'''
First of all, you need to download the mentioned libraries in this code.

I've used NLTK and newspaper libraries, to install these libraries on your computer,
open the terminal and apply these commands:

> pip install nltk
> pip3 install newspaper3k

Now, go ahead with me :)
'''

# Importing libraries

# Natural Language Toolkit, visit: https://www.nltk.org/
import nltk

# newspaper library. For more details, try to visit: https://newspaper.readthedocs.io/en/latest/
from newspaper import Article

'''
An example from Washington Post, with this title:
*** Health care workers worry about coronavirus protection ***
'''

url = 'https://www.washingtonpost.com/health/health-care-workers-worry-about-coronavirus-protection/2020/03/05/be04d5a8-5e33-11ea-9055-5fa12981bbbf_story.html'
article = Article(url)

article.download()
article.parse()
nltk.download('punkt')
article.nlp()

# Title...
title = article.title
print(f"\nTitle:\n{title}")

# Author...
author = article.authors
print(f"\nAuthor/Authors:\n{author}")

# Publish date...
publishDate = article.publish_date
print(f"\nPublish date:\n{publishDate}")

# Top Image of this article...
topImg = article.top_image
print(f"\nTop image:\n{topImg}")

# Text of the article...
text = article.text[:150]  # 150 character from the whole article
print(f"\nThe text (first 150 character) of this article is:\n{text}")

# The summary of the article...
summary = article.summary
print(f"\nThe summary of this article is:\n{summary}\n")

print("Be safe guys,\nMeqdad")
'''
Hope you enjoy it!

Homework :-)

* Add some features to this simple program that makes the user able to insert the link of a new article.
* Create a menu for these data, so the user can request the exact information about the chosen article.

'''
