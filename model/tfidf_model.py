"""
TF-IDF and Cosine Similarity Model
Calculates text similarity between resume and job description
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class TFIDFModel:
    """Calculate TF-IDF similarity between texts"""
    
    def __init__(self):
        """Initialize the TF-IDF vectorizer with optimal parameters"""
        self.vectorizer = TfidfVectorizer(
            max_features=1000,      # Maximum features to extract
            stop_words='english',   # Remove common English words
            ngram_range=(1, 2),     # Use unigrams and bigrams
            min_df=1,               # Minimum document frequency
            max_df=1.0              # Maximum document frequency
        )
        self.fitted = False
    
    def calculate_similarity(self, resume_text, job_description):
        """
        Calculate cosine similarity between resume and job description
        
        Args:
            resume_text (str): Cleaned resume text
            job_description (str): Job description text
            
        Returns:
            float: Similarity score between 0 and 100
        """
        try:
            # Combine texts for fitting vocabulary
            combined_texts = [resume_text, job_description]
            
            # Fit and transform
            tfidf_matrix = self.vectorizer.fit_transform(combined_texts)
            
            # Calculate cosine similarity
            similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
            
            # Extract similarity score and convert to percentage
            similarity_score = similarity_matrix[0][0]
            percentage_score = round(similarity_score * 100, 2)
            
            return percentage_score
        
        except Exception as e:
            print(f"Error calculating similarity: {str(e)}")
            return 0.0
    
    def get_top_features(self, text, n_features=10):
        """
        Get top TF-IDF features from text
        
        Args:
            text (str): Input text
            n_features (int): Number of top features to return
            
        Returns:
            list: List of top features
        """
        try:
            # Transform text
            tfidf_vector = self.vectorizer.fit_transform([text])
            
            # Get feature names
            feature_names = self.vectorizer.get_feature_names_out()
            
            # Get indices of top features
            indices = np.argsort(tfidf_vector.toarray()[0])[-n_features:][::-1]
            
            # Return top features
            top_features = [feature_names[i] for i in indices if tfidf_vector.toarray()[0][i] > 0]
            
            return top_features[:n_features]
        
        except Exception as e:
            print(f"Error getting top features: {str(e)}")
            return []


# Create global instance
tfidf_model = TFIDFModel()


def calculate_resume_similarity(resume_text, job_description):
    """
    Wrapper function to calculate similarity
    
    Args:
        resume_text (str): Cleaned resume text
        job_description (str): Job description text
        
    Returns:
        float: Similarity score (0-100)
    """
    return tfidf_model.calculate_similarity(resume_text, job_description)
