
def preprocess(df):
    try:
        import re
        from konlpy.tag import Komoran  # 한국어 형태소 분석기 (명사 추출) 패키지
        from collections import Counter # 단어 빈도 개수 세기 패키지
        import pandas as pd             # 데이터 프레임 처리 패키지

        # 데이터프레임을 리스트로 변경
        df_list = df['연설문'].tolist()
        # 리스트 -> 문자열로 변경 및 분할                  
        text = ' '.join(df_list)
    
        # 영문자, 숫자, 한글, 공백을 제외한 모든 문자를 찾아 제거
        pattern = r'[^a-zA-Z가-힣\s]'
        text = re.sub(pattern, '', text)  
        print('패턴 제거 완료')

        # 명사만 추출하기
        komoran = Komoran()
        nouns = komoran.nouns(text)
        print('명사추출 완료')
        # 단어 빈도 개수 세기
        df_words_counts = Counter(nouns)
        print('빈도 개수 세기 완료')
        # 1개 미만 단어 제외 및 내림차순 정렬
        df = df_words_counts.most_common()
        df = pd.DataFrame(df, columns=["word", "count"])
        selected = df['word'].str.len() > 1
        return df[selected]
    except Exception as e:
        print(e)
        empty = []
        return pd.DataFrame({'word':empty, 'count':empty})
    
        
    
        
        
