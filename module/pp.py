
# def select_add_for_excel_from_folder(folder_path, column_name):
#     try:
#         import pandas as pd # 데이터 프레임 처리 패키지
#         import os           # 폴더 경로 조작 패키지

#         # 모든 엑셀 파일을 저장할 리스트
#         combined_column = []
    
#         # 폴더 내의 파일 목록 가져오기
#         file_list = os.listdir(folder_path)
    
#         # 각 파일에 대해 처리
#         for file_name in file_list:
#             # 파일 경로 생성
#             file_path = os.path.join(folder_path, file_name)
        
#         # 파일 확장자가 엑셀인지 확인
#         if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
#             # 엑셀 파일을 데이터프레임으로 불러오기
#             pd.read_excel(file_path)
            
#             # # 지정된 열(column)을 추출하여 리스트에 추가
#             # if column_name in df.columns:
#             #     selected_column = df[column_name].tolist()
#             #     combined_column.extend(selected_column)
    
#     except Exception as e:
#         print(e)

#%%
def preprocess(df):
    try:
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
    
        
    
        
        
