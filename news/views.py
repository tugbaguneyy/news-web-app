import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.contrib import messages
from .services.news_service import NewsAPIService
from .serializers.news_serializer import NewsArticleSerializer
from .utils.constants import NEWS_CATEGORIES, CATEGORY_DISPLAY_NAMES

logger = logging.getLogger(__name__)

class NewsListView(TemplateView):
    """Ana sayfa - haber listesi"""
    template_name = 'news/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Query parametrelerini al
        category = self.request.GET.get('category')
        page = self.request.GET.get('page', 1)
        
        logger.info(f"Fetching news for category: {category}")
        
        # NewsAPI service'i kullan
        news_service = NewsAPIService()
        news_data = news_service.get_top_headlines(category=category)
        
        # Debug için log ekle
        logger.info(f"API Response status: {news_data.get('status')}")
        logger.info(f"API Response message: {news_data.get('message', 'No message')}")
        logger.info(f"Articles count: {len(news_data.get('articles', []))}")
        
        if news_data.get('status') == 'error':
            error_msg = f"API Hatası: {news_data.get('message', 'Bilinmeyen hata')}"
            messages.error(self.request, error_msg)
            logger.error(f"NewsAPI Error: {news_data}")
            articles = []
        else:
            # Verileri serialize et
            raw_articles = news_data.get('articles', [])
            articles = NewsArticleSerializer.serialize_articles(raw_articles)
            logger.info(f"Serialized articles count: {len(articles)}")
        
        # Pagination
        paginator = Paginator(articles, 12)  # Sayfa başına 12 haber
        page_obj = paginator.get_page(page)
        
        # Kategorileri isim ile birlikte hazırla
        categories_with_names = [
            {'key': cat, 'name': CATEGORY_DISPLAY_NAMES.get(cat, cat)}
            for cat in NEWS_CATEGORIES
        ]
        
        context.update({
            'articles': page_obj,
            'categories_with_names': categories_with_names,
            'current_category': category,
            'current_category_name': CATEGORY_DISPLAY_NAMES.get(category, category) if category else None,
            'total_results': news_data.get('totalResults', 0),
        })
        
        return context

class NewsSearchView(TemplateView):
    """Haber arama"""
    template_name = 'news/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        query = self.request.GET.get('q', '').strip()
        page = self.request.GET.get('page', 1)
        
        if not query:
            context.update({
                'articles': [],
                'search_query': '',
                'categories_with_names': [
                    {'key': cat, 'name': CATEGORY_DISPLAY_NAMES.get(cat, cat)}
                    for cat in NEWS_CATEGORIES
                ],
            })
            return context
        
        # Arama yap
        news_service = NewsAPIService()
        news_data = news_service.search_news(query=query)
        
        if news_data.get('status') == 'error':
            messages.error(self.request, 'Arama sırasında bir hata oluştu.')
            articles = []
        else:
            raw_articles = news_data.get('articles', [])
            articles = NewsArticleSerializer.serialize_articles(raw_articles)
        
        # Pagination
        paginator = Paginator(articles, 12)
        page_obj = paginator.get_page(page)
        
        categories_with_names = [
            {'key': cat, 'name': CATEGORY_DISPLAY_NAMES.get(cat, cat)}
            for cat in NEWS_CATEGORIES
        ]
        
        context.update({
            'articles': page_obj,
            'search_query': query,
            'categories_with_names': categories_with_names,
            'total_results': news_data.get('totalResults', 0),
        })
        
        return context