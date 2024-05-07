from rake_nltk import Rake

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

# Extraction given the text.
r.extract_keywords_from_text("Artificial Intelligence (AI) is revolutionizing industries, driving innovation, and transforming the way we live and work. From autonomous vehicles to personalized healthcare and algorithmic decision-making, AI has the potential to bring about unprecedented advancements. However, with great power comes great responsibility. As AI technologies continue to evolve, it is imperative that we prioritize ethics to ensure that these advancements are made responsibly and ethically. Accountability and transparency are crucial components of ethical AI. It is essential that AI developers and organizations are held accountable for the decisions made by AI systems. This includes providing explanations for AI-driven decisions and ensuring transparency in the decision-making process. Mechanisms such as algorithmic auditing and explainable AI can help promote accountability and transparency, enabling users to understand how AI systems work and the factors influencing their decisions.")

# Extraction given the list of strings where each string is a sentence.
# r.extract_keywords_from_sentences(<list of sentences>)

# To get keyword phrases ranked highest to lowest.
# print(r.get_ranked_phrases()[0:5])

# To get keyword phrases ranked highest to lowest with scores.
print(r.get_ranked_phrases_with_scores()[0:5])