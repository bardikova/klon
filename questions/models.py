# coding: utf-8
from __future__ import unicode_literals
from django.db import models
import random
# Create your models here.

STATUS_CHOICES = (
	('new', u'Новый'),
	('published', u'Опубликован'),
	('decline', u'Отклонен'),
	('duplicate', u'Дубляж'),
)

class Questions(models.Model):
	request_number = models.IntegerField(u'Номер запроса',unique=True)
	title = models.CharField(u'Тема',max_length=255)
	text = models.CharField(u'Текст',max_length=255)
	answer = models.TextField(u'Ответ', null=True, blank=True)
	phone_number = models.CharField(u'Телефон',max_length=12)
	user_email = models.EmailField(u'Почта')
	status = models.CharField(u'Статус', max_length=30, choices=STATUS_CHOICES)
	update_at = models.DateTimeField(u'Обновлено', auto_now = True)
	created_at = models.DateTimeField(u'Создано', auto_now_add=True)
	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.pk:
			self.request_number = 1000 + random.randint(1000, 9999)
			max_tries = 100
			request_number_not_unique = True
			while request_number_not_unique:
				self.request_number = 1000 + random.randint(1000, 9999)
				if max_tries == 0:
				#send email to tech staff
					break
				if Questions.objects.filter(request_number=self.request_number).count() == 0:
					request_number_not_unique = False
				max_tries -= 1
		# print "This is args", args
		# print "This is kwargs", kwargs
		# self.request_number = 1000 + random.randint(1000, 9999)
		super(Questions, self).save(*args, **kwargs)
	# try:
	# 	Questions.objects.get(request_number=self.request_number)
	# except Questions.DoesNotExist:
	# 	self.request_number = 1000 + random.randint(1000, 9999)
	# 	super(Questions, self).save(*args, **kwargs)




# try: # то что мы пытаемся запустить
# 	pass
# except Exception, e: # действие по умолчанию, если ловим ошибку
# 	raise