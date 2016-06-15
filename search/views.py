from django.shortcuts import render

# Create your views here.
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import RegexAnalyzer
from whoosh.analysis import Tokenizer, Token
import jieba
from notice.models import Notice
from forum.models import Topic
from homework.models import Homework


class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        assert isinstance(value, text_type), "%r is not unicode" % value
        t = Token(positions, chars, removestops=removestops, mode=mode,
                  **kwargs)
        seglist = jieba.cut(value, cut_all=False)  # 使用结巴分词库进行分词
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
                t.endchar = start_char + value.find(w) + len(w)
            yield t  # 通过生成器返回每个分词的结果token


def ChineseAnalyzer():
    return ChineseTokenizer()


def search(request):
    keyword = str(request.POST['search'])
    analyzer = ChineseAnalyzer()
    schema = Schema(title=TEXT(stored=True), id=NUMERIC(stored=True), author=TEXT(stored=True),
                    content=TEXT(stored=True, analyzer=analyzer), flag=NUMERIC(stored=True, default=0))
    ix = create_in('D:\Graduation Project\CourseWebsite\indexdir', schema)
    notice = Notice.objects.all()
    topic = Topic.objects.all()
    homework = Homework.objects.all()

    writer = ix.writer()
    for n in notice:
        writer.add_document(title=n.title, author=n.author, content=n.content, id=n.id, flag=0)
    for t in topic:
        writer.add_document(title=t.title, author=t.author, content=t.content, id=t.id, flag=t.is_topic)
    for h in homework:
        writer.add_document(title=h.title, author=h.author, content=h.content, id=h.id, flag=h.is_work)
    writer.commit()

    searcher = ix.searcher()
    content_result = searcher.find('content', keyword)
    author_result = searcher.find('author', keyword)
    title_result = searcher.find('title', keyword)
    num = len(content_result) + len(title_result) + len(author_result)
    print(title_result)
    content = {
        'title_results': title_result,
        'content_results': content_result,
        'author_results': author_result,
        'num': num,
    }
    return render(request, 'search.html', content)
