





#make a virtual env for this project.
from flask import Flask,render_template
from newsapi import NewsApiClient





app = Flask(__name__)
# navbar
@app.route('/')
def navbar():
    
    return render_template("navbar.html")
# create a route function 

@app.route('/')
def home():
    #enter client id and api-key for authorization
    
    newsapi = NewsApiClient(api_key="a082fedfb160404da55fe01229c927db")
    # for top headlines
    # top_headlines = newsapi.get_top_headlines(sources=[""])
    top_headlines = newsapi.get_top_headlines(sources='bbc-news')
    # fetch all the auricles of top headline
    #for all the main auticles we will code 
    # all_articles = newsapi.get_everything(sources=[""])
    all_articles = newsapi.get_everything(sources='bbc-news')
    
    t_articles = top_headlines['articles']
    
    #fetch all the articles
    a_articles = all_articles['articles']
    
    # make a list contents of all articles
    news = []
    desc = []
    img= []
    p_date = []
    url = []
    
    #fetch all the contents of all articles
    
    for i in range(len(t_articles)):
        main_article = t_articles[i]
        
        # atlast append all the contents
        
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        
    news_all = []
    desc_all = []
    img_all= []
    p_date_all = []
    url_all = []
    
    for j in range(len(a_articles)):
        a_article = a_articles[j]
        
        
        news_all.append(a_article['title'])
        desc_all.append(a_article['description'])
        img_all.append(a_article['urlToImage'])
        p_date_all.append(a_article['publishedAt'])
        url_all.append(a_article['url'])
        
        
        
        
        #make a zip for the contents of all articles
        
        contents = zip(news, desc, img, p_date, url)
        
        friend = zip(news_all, desc_all, img_all, p_date_all, url_all)
    #pass it in rendered file.
    
    
    return render_template('home.html',contents = contents,friend=friend)



# cnn

@app.route('/index')
def index():
    #enter client id and api-key for authorization
    
    newsapi = NewsApiClient(api_key="a082fedfb160404da55fe01229c927db")
    # for top headlines
    # top_headlines = newsapi.get_top_headlines(sources=[""])
    top_headlines = newsapi.get_top_headlines(sources='cnn')
    # fetch all the auricles of top headline
    #for all the main auticles we will code 
    # all_articles = newsapi.get_everything(sources=[""])
    all_articles = newsapi.get_everything(sources='cnn')
    
    t_articles = top_headlines['articles']
    
    #fetch all the articles
    a_articles = all_articles['articles']
    
    # make a list contents of all articles
    news = []
    desc = []
    img= []
    p_date = []
    url = []
    
    #fetch all the contents of all articles
    
    for i in range(len(t_articles)):
        main_article = t_articles[i]
        
        # atlast append all the contents
        
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        
    news_all = []
    desc_all = []
    img_all= []
    p_date_all = []
    url_all = []
    
    for j in range(len(a_articles)):
        a_article = a_articles[j]
        
        
        news_all.append(a_article['title'])
        desc_all.append(a_article['description'])
        img_all.append(a_article['urlToImage'])
        p_date_all.append(a_article['publishedAt'])
        url_all.append(a_article['url'])
        
        
        
        
        #make a zip for the contents of all articles
        
        contents = zip(news, desc, img, p_date, url)
        
        friend = zip(news_all, desc_all, img_all, p_date_all, url_all)
    #pass it in rendered file.
    
    
    return render_template('index.html',contents = contents,friend=friend)



if __name__ == '__main__':
    app.run(debug=True)
    

#   second way




# from flask import Flask,render_template
# from newsapi.newsapi_client import NewsAPIClient

# app = Flask(__name__)

# @app.route("/")
# def index():
#     newsapi= NewsAPIClient(api_key="a082fedfb160404da55fe01229c927db")
    
#     topheadlines= newsapi.get_top_headlines(sources="BBC News")
    
    
    
#     articles = topheadlines['articles']
    
#     description = []
#     news= []
#     img=[]
    
#     for i in range(len(articles)):
#         myarticles = [articles[i]]
        
#         news.append(myarticles['title'])
#         description.append(myarticles['description'])
#         img.append(myarticles['"urlToImage'])
        
        
        
#     mylist =  zip(news, img,description)
    
#     return render_template("index.html",context=mylist)
        
# if __name__ == '__main__':
#     app.run(debug=True)
    