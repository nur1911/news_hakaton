from django.db import models

LANGUAGE = (('KR','КЫРГЫЗСКИЙ'),('RU','РУССКИЙ'))

class News_Details(models.Model):
    title = models.CharField('Оглавление',max_length=1000)
    header_title = models.CharField('Название',max_length=1000)
    text = models.TextField('Текст новости')
    filter = models.ForeignKey('Filter', on_delete=models.CASCADE)
    add_date = models.DateField('Дата начало')
    edit_date = models.DateField('Дата изменения')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def image(self):
        return Images.objects.filter(news_detail=self).first()

    def filter(self):
        return Filter.objects.filter(news_detail=self).first()

    def language(self):
        return Language.objects.filter(news_detail=self).first()


class Images(models.Model):
    url = models.URLField()
    order_num = models.IntegerField()
    active = models.BooleanField(default=True)
    news_detail = models.ForeignKey(News_Details, on_delete=models.DO_NOTHING)




class Filter(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='category')


    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=2, choices=LANGUAGE)








