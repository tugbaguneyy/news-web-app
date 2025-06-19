import requests
from typing import Dict, List, Optional
from django.conf import settings
from django.core.cache import cache
from ..utils.constants import NEWS_CATEGORIES

class NewsAPIService:
    """NewsAPI ile etkileşim için service class"""
    
    def __init__(self):
        self.api_key = settings.NEWS_API_KEY
        self.base_url = settings.NEWS_API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({'X-API-Key': self.api_key})
    
    def get_top_headlines(self, category: Optional[str] = None, 
                         country: str = 'us', page_size: int = 20) -> Dict:
        """En son haberleri getir"""
        cache_key = f"top_headlines_{category}_{country}_{page_size}"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return cached_data
        
        params = {
            'country': country,
            'pageSize': page_size,
        }
        
        if category and category in NEWS_CATEGORIES:
            params['category'] = category
        
        try:
            response = self.session.get(
                f"{self.base_url}/top-headlines",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            # 15 dakika cache
            cache.set(cache_key, data, 60 * 15)
            return data
            
        except requests.RequestException as e:
            return {'status': 'error', 'message': str(e), 'articles': []}
    
    def search_news(self, query: str, page_size: int = 20) -> Dict:
        """Haber arama"""
        cache_key = f"search_{query}_{page_size}"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return cached_data
        
        params = {
            'q': query,
            'pageSize': page_size,
            'language': 'tr',
            'sortBy': 'publishedAt'
        }
        
        try:
            response = self.session.get(
                f"{self.base_url}/everything",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            cache.set(cache_key, data, 60 * 10)  # 10 dakika cache
            return data
            
        except requests.RequestException as e:
            return {'status': 'error', 'message': str(e), 'articles': []}