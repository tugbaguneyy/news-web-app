from typing import Dict, List

class NewsArticleSerializer:
    """Haber verilerini temizleme ve dönüştürme"""
    
    @staticmethod
    def serialize_article(article: Dict) -> Dict:
        """Tek bir haberi serialize et"""
        return {
            'title': article.get('title', 'Başlık bulunamadı'),
            'description': article.get('description', ''),
            'url': article.get('url', ''),
            'image_url': article.get('urlToImage', ''),
            'source': article.get('source', {}).get('name', 'Bilinmeyen kaynak'),
            'published_at': article.get('publishedAt', ''),
            'author': article.get('author', ''),
        }
    
    @staticmethod
    def serialize_articles(articles: List[Dict]) -> List[Dict]:
        """Haber listesini serialize et"""
        return [
            NewsArticleSerializer.serialize_article(article) 
            for article in articles if article.get('title')
        ]