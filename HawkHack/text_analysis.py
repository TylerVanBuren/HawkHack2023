#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:50:08 2023

@author: tyler
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Quotes database
quotes = [
    "Don't let yesterday take up too much of today."
    ,"You are never too old to set another goal or to dream a new dream."
    ,"The only way to do great work is to love what you do."
    ,"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."
    ,"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."
    ,"It does not matter how slowly you go as long as you do not stop."
    ,"The future belongs to those who believe in the beauty of their dreams."
    ,"I can't change the direction of the wind, but I can adjust my sails to always reach my destination."
    ,"Success is not final, failure is not fatal: it is the courage to continue that counts."
    ,"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."
    ,"Believe you can and you're halfway there."
    ,"Happiness is not something ready made. It comes from your own actions."
    ,"We may encounter many defeats but we must not be defeated."
    ,"The only way to do great work is to love what you do."
    ,"The only limit to our realization of tomorrow will be our doubts of today."
    ,"The greatest glory in living lies not in never falling, but in rising every time we fall."
    ,"Your time is limited, don't waste it living someone else's life."
    ,"The best way to predict your future is to create it."
    ,"It is during our darkest moments that we must focus to see the light."
    ,"You miss 100% of the shots you don't take."
    ,"If you want to live a happy life, tie it to a goal, not to people or things"
    ,"Don't watch the time on the clock; do what it does. Keep going."
    ,"The difference between ordinary and extraordinary is that little extra"
    ,"Strive not to be a success, but rather to be of value"
    ,"Happiness is not something you postpone for the future; it is something you design for the present"
    ,"If you're going through hell, keep going"
    ,"We can't help everyone, but everyone can help someone"
    ,"The only way to have a good day is to start it with a positive attitude"
    ,"The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty"
    ,"The best preparation for tomorrow is doing your best today"

]
def getQuote(user_ailment):
    # Calculate TF-IDF scores for tokens
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([user_ailment] + quotes)
    
    # Calculate cosine similarity scores
    cosine_similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])[0]
    
    # Sort quotes by similarity score
    sorted_quotes = [quote for (similarity, quote) in sorted(zip(cosine_similarities, quotes), reverse=True)]
    
    # Choose the best quote
    selected_quote = sorted_quotes[0]
    
    return(selected_quote)
