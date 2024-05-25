from backend.server.api.product import ProductDBAPI
from sklearn.metrics.pairwise import cosine_similarity
import asyncio
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk,copy,time
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
stop_words_en = set(stopwords.words('english'))
stop_words_vi = set()
# stop_words_vi = set(stopwords.words('vietnamese'))
def get_basic(data : dict) -> list:
    result = []
    i=0
    while(True):
        key = 'basic_info_{}'.format(i)
        if (key in data):
            result.append(data[key])
            i+=1
        else:
            break
    return result
def preprocess_test(text : str):
    text = text.lower()
    text = re.sub(r'\W',' ',text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words_en and word not in stop_words_vi]
    return tokens
async def main():
    api = ProductDBAPI()
    api.start()
    test_products = await api.get_product_detail({
        'limit' : 1000,
        'mode' : None
    })
    basic_infos = []
    combined = []
    for test_product in test_products:
        basic_info = get_basic(test_product)
        combined.append(' '.join(basic_info))
        basic_infos.append(basic_info)
    
    vectorized = TfidfVectorizer(stop_words=list(stop_words_en))
    start = time.time()
    vectorized.fit_transform(combined)
    print('Fit time {}'.format(time.time()-start))
    
    tdidf_matrix1 = vectorized.transform([combined[0]])
    tdidf_matrix2 = vectorized.transform([combined[1]])
    
    similarity_matrix = cosine_similarity(tdidf_matrix1,tdidf_matrix2)
    
    print(similarity_matrix)
    
    # feature_names = vectorized.get_feature_names_out()
    
    # idf_values = vectorized.idf_
    
    # print('Feature names : ', feature_names )
    # print('IDF Values : ', idf_values)
    
    
    await api.stop()
asyncio.run(main())