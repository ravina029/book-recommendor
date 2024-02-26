import pickle
import streamlit as st 
import numpy as np

st.header("Book Recommender System using ML algorithm")
model=pickle.load(open("artifacts/model.pkl",'rb'))
bookname=pickle.load(open("artifacts/book_name.pkl",'rb'))
book_pivot=pickle.load(open("artifacts/book_pivot.pkl",'rb'))
final_rating=pickle.load(open("artifacts/final_rating.pkl",'rb'))




def poster(suggestion):
    bookname=[]
    id_index=[]
    poster_url=[]

    for book_id in suggestion:
        bookname.append(book_pivot.index[book_id])

    for name in bookname[0]:
        ids=np.where(final_rating['Book']==name)[0][0]
        id_index.append(ids)

    for idx in id_index:
        url=final_rating.iloc[idx]['url']
        poster_url.append(url)
    
    return poster_url
def recommend_book(bookname):
    books=[]
    book_id=np.where(book_pivot.index==bookname)[0][0]
    distance,suggestion=model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)

    poster_url=poster(suggestion)
    for i in range (len(suggestion)):
        book=book_pivot.index[suggestion[i]]
        for j in book:
            books.append(j)
    return books, poster_url
chosed_books=st.selectbox(
    "Select or Enter the name of the book",
    bookname

)

if st.button('Recommendation of Books'):
    recommended_book,poster_url=recommend_book(chosed_books)

    #for i in range(min(len(recommended_book), 5)):
        #st.text(recommended_book[i])
        #st.image(poster_url[i])

    #print("Length of recommended_book:", len(recommended_book))

    col1, col2, col3, col4, col5=st.columns(5)

    with col1:
        st.text(recommended_book[1])
        st.image(poster_url[1])
    
    with col2:
        st.text(recommended_book[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommended_book[3])
        st.image(poster_url[3])
    
    with col4:
        st.text(recommended_book[4])
        st.image(poster_url[4])
    
    with col5:
        st.text(recommended_book[5])
        st.image(poster_url[5])
    
    
    
    
    