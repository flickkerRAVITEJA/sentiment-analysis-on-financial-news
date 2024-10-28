import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download stopwords and wordnet resources
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    # Remove URLs and special characters
    text = re.sub(r"http\S+|[^a-zA-Z\s]", "", text.lower())
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    
    # Lemmatize words (convert them to their base form)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return " ".join(words)

# Example usage
sample_text = "The market is booming today! Visit https://example.com for more info."
print(clean_text(sample_text))  # Output: 'market booming today'
