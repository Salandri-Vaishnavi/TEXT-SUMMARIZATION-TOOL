from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize_article(text, num_sentences=50):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

# Example usage
if __name__ == "__main__":
    article = """
Dr. A.P.J. Abdul Kalam: The Missile Man of India and the People's President.
Dr. Avul Pakir Jainulabdeen Abdul Kalam, widely known as Dr. A.P.J. Abdul Kalam, was one of India's most revered scientists and the 
11th President of India. He was a symbol of humility, dedication, and brilliance, whose journey from a small town in Rameswaram to the
Rashtrapati Bhavan is an inspiring story of perseverance, patriotism, and a passion for education and nation-building. This essay explores
the life, contributions, and legacy of Dr. Abdul Kalam, who remains a guiding light for millions even after his passing.
Dr. Abdul Kalam was born on October 15, 1931, in the island town of Rameswaram in Tamil Nadu. His father, Jainulabdeen, was a boat owner 
and imam of a local mosque, and his mother, Ashiamma, was a homemaker. Despite growing up in a modest household, Kalam's parents instilled
in him the values of honesty, discipline, and hard work. From a young age, he displayed a keen interest in learning and showed exceptional 
curiosity about the world around him. In 2002, Dr. Abdul Kalam was elected as the 11th President of India. His presidency was marked
by humility, accessibility, and an unwavering focus on youth empowerment and education. Although a scientist by profession, Kalam was 
a peoples President, known for his down-to-earth nature and deep concern for the future of the country. Dr. A.P.J. Abdul Kalams life 
is a testament to the power of dreams, hard work, and humility. From a small town in Tamil Nadu to the highest office in the land, his
journey inspired generations of Indians to pursue excellence and serve the nation. A brilliant scientist, a visionary leader, a 
compassionate teacher, and above all, a true patriot—Dr. Kalam remains an eternal source of inspiration. He once said, “Dream, dream,
dream. Dreams transform into thoughts and thoughts result in action.” He didnt just preach those words; he lived them. In remembering
Dr. Kalam, we remember the very best of what India stands for—knowledge, progress, unity, and hope. Post-Presidency and Vision:
After his presidency, Kalam dedicated his life to teaching, writing, and inspiring youth. He advocated for a strong, self-reliant India 
and laid out a vision in his books like India 2020, Wings of Fire, and Ignited Minds."Let us sacrifice our today so that our children 
can have a better tomorrow."He interacted with students across the country, encouraging them to innovate, think big, and contribute to
national development. On July 27, 2015, while giving a lecture at IIM Shillong, Dr. Kalam collapsed due to cardiac arrest. He passed
away doing what he loved most—teaching and inspiring students. "End is not the end, in fact E.N.D. means 'Effort Never Dies Dr. A.P.J.
Abdul Kalam remains a symbol of simplicity, integrity, and vision. His life continues to inspire millions to dream big and serve the
nation with honesty and courage. He believed in the power of education, hard work, and dreaming beyond limitations.
    """
    
    print("Original Length:", len(article.split()), "words")
    summary = summarize_article(article, num_sentences=15)# Adjust this number to make it shorter or longer
    print("\nSummary:\n", summary)
