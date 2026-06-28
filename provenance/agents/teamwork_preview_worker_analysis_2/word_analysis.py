import os
import re
import pandas as pd

# Paths to the target files
FILES_TO_ANALYZE = {
    'ipn-samledokument.md': r'C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/docs/reference/ipn-samledokument.md',
    'ipn-hovedokument.md': r'C:/Users/larse/Documents/Interne prosjekter/Vibs/vibs-boligpass/docs/reference/ipn-hovedokument.md'
}

# Buzzword and jargon patterns
PATTERNS = {
    'AI buzzword': {
        'AI': r'\b(ai|AI)\b',
        'kunstig intelligens': r'\bkunstig\s+intelligens\b',
        'agent': r'\bagent(er|en|ene|s)?\b',
        'maskinlæring': r'\bmaskinlæring(s)?\b',
        'algoritme': r'\balgoritme(r|n|ne|s)?\b',
        'llm': r'\bllm(s)?\b',
        'gpt': r'\bgpt(s)?\b',
        'neural': r'\bneural(e|t)?\b',
        'deep learning': r'\bdeep\s+learning\b'
    },
    'Jargon': {
        'synergi': r'\bsynergi(er|en|ene|s)?\b',
        'transformasjon': r'\btransformasjon(er|en|ene|s)?\b',
        'optimalisering': r'\boptimalisering(er|en|ene|s)?\b',
        'robust': r'\brobust(e)?\b',
        'holistisk': r'\bholistisk(e)?\b',
        'digitalisering': r'\bdigitalisering(er|en|ene|s)?|digitaliser(t|te|e)\b',
        'siloer': r'\bsilo(er|en|ene|s)?\b',
        'syntesen': r'\bsyntese(n|r|ne|s)?\b',
        'robusthet': r'\brobusthet(en)?\b',
        'operasjonalisert': r'\boperasjonaliser(t|e|ing|inger|ingen|ingene)\b'
    }
}

def clean_markdown(text):
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Convert markdown links [text](url) to text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Convert bold/italic
    text = re.sub(r'\*\*([^*]+)\*\*|__([^_]+)__', r'\1\2', text)
    text = re.sub(r'\*([^*]+)\*|_([^_]+)_', r'\1\2', text)
    return text

def get_sentences(text):
    cleaned = clean_markdown(text)
    # Replace multiple spaces/newlines with single space
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    # Split sentences avoiding common abbreviations
    abbreviations = ['ca.', 'mrd.', 'stk.', 'kr.', 'al.', 'no.', 'wp.', 'ap.', 'sek.', 'fig.', 'tab.', 'vs.']
    for abbr in abbreviations:
        placeholder = abbr.replace('.', '___')
        cleaned = re.sub(rf'\b{abbr}', placeholder, cleaned, flags=re.IGNORECASE)
    
    # Also handle numbers like 3.3, 12.2, 12.5
    cleaned = re.sub(r'(\d)\.(\d)', r'\1__dot__\2', cleaned)
    
    # Now split on actual sentence endings
    raw_sentences = re.split(r'(?<=[.!?])\s+', cleaned)
    
    sentences = []
    for s in raw_sentences:
        s = s.strip()
        if not s:
            continue
        # Restore dots
        for abbr in abbreviations:
            placeholder = abbr.replace('.', '___')
            s = re.sub(rf'\b{placeholder}', abbr, s, flags=re.IGNORECASE)
        s = s.replace('__dot__', '.')
        sentences.append(s)
    return sentences

def count_words(sentence):
    # Count words in a sentence by splitting on whitespace, ignoring punctuation
    words = re.findall(r'\b[\w-]+\b', sentence) # allow hyphens inside words
    return len(words), words

def analyze_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Analyze terms
    term_counts = []
    for category, terms in PATTERNS.items():
        for term, pattern in terms.items():
            matches = re.findall(pattern, content, flags=re.IGNORECASE)
            count = len(matches)
            term_counts.append({
                'Category': category,
                'Term': term,
                'Count': count
            })
            
    # Analyze sentences and word lengths
    sentences = get_sentences(content)
    complex_sentences = []
    long_words = []
    
    for sentence in sentences:
        word_count, words = count_words(sentence)
        if word_count > 25:
            complex_sentences.append((sentence, word_count))
        for w in words:
            if len(w) > 15:
                long_words.append(w)
                
    return {
        'term_counts': term_counts,
        'complex_sentences': complex_sentences,
        'long_words': long_words,
        'sentences_count': len(sentences)
    }

def main():
    all_term_data = []
    summary_reports = {}
    
    for filename, filepath in FILES_TO_ANALYZE.items():
        print(f"\n==================================================")
        print(f"Analyzing {filename}...")
        results = analyze_file(filepath)
        if results is None:
            continue
            
        summary_reports[filename] = results
        print(f"Total sentences: {results['sentences_count']}")
        print(f"Complex sentences (>25 words): {len(results['complex_sentences'])}")
        print(f"Long words (>15 chars): {len(results['long_words'])}")
        
        # Add filename column to term counts
        for data in results['term_counts']:
            data['File'] = filename
            all_term_data.append(data)
            
        print("\nComplex Sentences (>25 words):")
        for s, count in sorted(results['complex_sentences'], key=lambda x: x[1], reverse=True):
            print(f"- [{count} words] {s}")
            
        print("\nLong Words (>15 chars):")
        print(sorted(list(set(results['long_words']))))
        
    # Create pandas DataFrame for term counts
    df = pd.DataFrame(all_term_data)
    df_pivot = df.pivot(index=['Category', 'Term'], columns='File', values='Count').reset_index()
    print("\nSummary of Term Counts:")
    print(df_pivot.to_string(index=False))

if __name__ == '__main__':
    main()
