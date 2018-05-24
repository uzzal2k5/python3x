from allauth import models
from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.db import models
import time, datetime
from decimal import Decimal
from django.db.models import Q
from model_utils import Choices
# Create your models here.
from django.utils import timezone


class Post(models.Model):
    posturl = models.CharField(max_length=255, default='')
    company = models.CharField(max_length=45)
    status_id = models.CharField(db_index=True,max_length=45)
    status_message = models.TextField(blank=True, null=True)
    status_published = models.DateTimeField(auto_now_add=True, blank=True)
    num_reactions = models.IntegerField()
    num_comments = models.IntegerField()
    num_shares = models.IntegerField()
    num_likes = models.IntegerField()
    num_loves = models.IntegerField()
    num_wows = models.IntegerField()
    num_hahas = models.IntegerField()
    num_sads = models.IntegerField()
    num_angrys = models.IntegerField()
    status = models.IntegerField(default=1)
    fans_comments = models.IntegerField(default=1)
    author_comments = models.IntegerField(default=1)
    total_comments = models.IntegerField(default=1)
    user = models.ForeignKey(User, blank=True)
    postimg = models.TextField(blank=True, null=True, default='')
    post_status = models.IntegerField(default=0)

    def __str__(self):
        return self.status_id


class Comment(models.Model):
    comment_message = models.TextField(blank=True, null=True)
    status_id = models.CharField(db_index=True,max_length=45)
    negative = models.IntegerField()
    positive = models.IntegerField()
    neutral = models.IntegerField()
    model_sent = models.IntegerField(default=0)

    query = models.IntegerField()
    complain = models.IntegerField()
    appreciation = models.IntegerField()
    feedback = models.IntegerField(default=0)
    feedbackneg = models.IntegerField()
    feedbackpos = models.IntegerField()
    spam = models.IntegerField()
    wom = models.IntegerField()
    model_com = models.IntegerField(default=0)

    pi = models.IntegerField()
    npi = models.IntegerField(default=0)
    notpi = models.IntegerField(default=0)
    model_int = models.IntegerField(default=0)

    product_service = models.IntegerField()
    after_sales = models.IntegerField()
    campaign_offers = models.IntegerField()
    others = models.IntegerField()
    model_cat = models.IntegerField(default=0)

    comment_author = models.CharField(max_length=45, default='')
    author_url = models.CharField(max_length=45, default='')
    comment_published = models.DateTimeField(auto_now_add=True)
    comment_likes = models.IntegerField(default=0)

    company = models.CharField(max_length=45, default='')
    comment_id = models.CharField(max_length=45, default='')
    misclassified = models.IntegerField(default=0)
    comment_status = models.IntegerField(default=0)

    def as_dict(self):
        """
        Create data for datatables ajax call.
        """
        return {'comment_message': self.comment_message,
                'status_id': self.status_id,
                'company': self.company,
                }

    @property
    def campaign(self):
        return Post.objects.filter(status_id=self.status_id).first().status_message

    def __str__(self):
        return self.status_id


ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'comment_message'),
    ('2', 'status_id'),
    ('3', 'comment_published'),
    ('4', 'comment_author'),
)


def query_musics_by_args(status_id,**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Comment.objects.filter(status_id=status_id)
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) | Q(comment_message__icontains=search_value) | Q(comment_published__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class UserGroupList(models.Model):
    name = models.CharField(max_length=45, default='')
    facebook_name = models.CharField(max_length=45, default='')
    profile_img = models.ImageField(upload_to='img/profile/%Y/%m/',default='default.jpg')

    def __str__(self):
        return self.name


class UserGroupPermission(models.Model):
    user = models.ForeignKey(User, blank=True, default='1')
    group = models.ForeignKey(UserGroupList, blank=True, default='')
    groupadmin = models.CharField(max_length=45, default='1')
    limit = models.CharField(max_length=45,default='')
    # userip = models.CharField(max_length=45, default='')
    staus = models.CharField(max_length=45, default='1')

    def __str__(self):
        return "grouppermission"


class UserLog(models.Model):
    todaydate = models.DateTimeField(auto_now_add=True)
    ugroup = models.ForeignKey(UserGroupList, blank=True, default=1)
    user = models.ForeignKey(User)
    logintime = models.DateTimeField(auto_now_add=True)
    logouttime = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=255)
    urlreq = models.IntegerField(default=0)

    def __str__(self):
        return self.ip


class NewUrl(models.Model):
    url = models.CharField(max_length=255)
    user = models.CharField(max_length=45)
    comName = models.CharField(max_length=45, default='', blank=True)
    urltime = models.DateTimeField(blank=True, auto_now=True)
    statusid = models.CharField(max_length=45)
    ugroup = models.ForeignKey(UserGroupList, blank=True, default=1)

    def __str__(self):
        return self.url


# DATE RANGE
class DateRangeNewUrl(models.Model):
    url = models.CharField(max_length=255)
    user = models.CharField(max_length=45)
    comName = models.CharField(max_length=45, default='', blank=True)
    urltime = models.DateTimeField(blank=True, auto_now=True)
    startdate = models.DateTimeField(blank=True)
    enddate = models.DateTimeField(blank=True)
    statusid = models.CharField(max_length=45)
    ugroup = models.ForeignKey(UserGroupList, blank=True, default=1)

    def __str__(self):
        return self.url


class KeywordUrl(models.Model):
    url = models.CharField(max_length=255)
    user = models.CharField(max_length=45)
    comName = models.CharField(max_length=45, default='', blank=True)
    urltime = models.DateTimeField(blank=True, auto_now=True)
    startdate = models.DateTimeField(blank=True)
    enddate = models.DateTimeField(blank=True)
    statusid = models.CharField(max_length=45)
    keyword = models.CharField(max_length=45)
    ugroup = models.ForeignKey(UserGroupList, blank=True, default=1)

    def __str__(self):
        return self.url


class DateRangePost(models.Model):
    company = models.CharField(max_length=45)
    status_id = models.CharField(max_length=45)
    num_reactions = models.IntegerField()
    num_comments = models.IntegerField()
    num_shares = models.IntegerField()
    num_likes = models.IntegerField()
    num_loves = models.IntegerField()
    num_wows = models.IntegerField()
    num_hahas = models.IntegerField()
    num_sads = models.IntegerField()
    num_angrys = models.IntegerField()
    status = models.IntegerField(default=1)
    fans_comments = models.IntegerField(default=1)
    author_comments = models.IntegerField(default=1)
    total_comments = models.IntegerField(default=1)
    user = models.IntegerField(blank=True)

    def __str__(self):
        return self.status_id


class DateRangeComment(models.Model):
    comment_message = models.TextField(blank=True, null=True)
    status_id = models.CharField(max_length=45)
    negative = models.IntegerField()
    positive = models.IntegerField()
    neutral = models.IntegerField()
    model_sent = models.IntegerField(default=0)

    query = models.IntegerField()
    complain = models.IntegerField()
    appreciation = models.IntegerField()
    feedbackneg = models.IntegerField()
    feedbackpos = models.IntegerField()
    wom = models.IntegerField()
    spam = models.IntegerField()
    model_com = models.IntegerField(default=0)

    pi = models.IntegerField()
    npi = models.IntegerField(default=0)
    notpi = models.IntegerField(default=0)
    model_int = models.IntegerField(default=0)

    product_service = models.IntegerField()
    after_sales = models.IntegerField()
    campaign_offers = models.IntegerField()
    others = models.IntegerField()
    model_cat = models.IntegerField(default=0)

    comment_author = models.CharField(max_length=45, default='')
    comment_published = models.CharField(max_length=45, default='')
    comment_likes = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.comment_message


class Userdetails(models.Model):
    user = models.ForeignKey(User, default=1)
    phone = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    profilepic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.address


class RequestDemo(models.Model):
    firstname = models.CharField(max_length=45, default='')
    lastname = models.CharField(max_length=45, default='')
    email = models.EmailField(default='')
    contactnum = models.CharField(max_length=45, default='')
    organization = models.CharField(max_length=45, default='')
    message = models.TextField(blank=True,default='')

    def __str__(self):
        return self.email


class CampaignAnalysis(models.Model):
    company = models.CharField(max_length=45)
    status_id = models.CharField(max_length=45)
    status_message = models.TextField(blank=True, null=True)
    status_published = models.DateTimeField(auto_now_add=True, blank=True)
    num_reactions = models.IntegerField()
    num_comments = models.IntegerField()
    num_shares = models.IntegerField()
    num_likes = models.IntegerField()
    num_loves = models.IntegerField()
    num_wows = models.IntegerField()
    num_hahas = models.IntegerField()
    num_sads = models.IntegerField()
    num_angrys = models.IntegerField()
    fans_comments = models.IntegerField(default=1)
    author_comments = models.IntegerField(default=1)
    total_comments = models.IntegerField(default=1)
    response_ration = models.FloatField(default=1)
    negative = models.IntegerField(default=1)
    positive = models.IntegerField(default=1)
    neutral = models.IntegerField(default=1)
    ratiopos = models.FloatField(default=1)
    rationeg = models.FloatField(default=1)
    rationeu = models.FloatField(default=1)
    query = models.IntegerField(default=1)
    complain = models.IntegerField(default=1)
    appreciation = models.IntegerField(default=1)
    feedback = models.IntegerField(default=0)
    spam = models.IntegerField(default=1)
    wom = models.IntegerField(default=1)
    query_percentage = models.FloatField(default=1)
    complain_percentage = models.FloatField(default=1)
    appreciation_percentage = models.FloatField(default=1)
    feedback_percentage = models.FloatField(default=0)
    spam_percentage = models.FloatField(default=1)
    wom_percentage = models.FloatField(default=1)
    pi = models.IntegerField(default=1)
    pi_percentage = models.FloatField(default=0)
    npi = models.IntegerField(default=0)
    product_service = models.IntegerField(default=1)
    after_sales = models.IntegerField(default=1)
    campaign_offers = models.IntegerField(default=1)
    others = models.IntegerField(default=1)
    product_service_percentage = models.FloatField(default=1)
    after_sales_percentage = models.FloatField(default=1)
    campaign_offers_percentage = models.FloatField(default=1)
    others_percentage = models.FloatField(default=1)
    dropout_percentage = models.FloatField(default=0)
    post_user = models.ForeignKey(User, blank=True)
    postimg = models.TextField(blank=True, null=True, default='')
    ps_pos = models.IntegerField(default=0)
    ps_neg = models.IntegerField(default=0)
    ps_neu = models.IntegerField(default=0)
    ps_query = models.IntegerField(default=0)
    ps_complain = models.IntegerField(default=0)
    ps_appreciation = models.IntegerField(default=0)
    ps_neg_fed = models.IntegerField(default=0)
    ps_pos_fed = models.IntegerField(default=0)
    total_ps = models.IntegerField(default=0)
    as_pos = models.IntegerField(default=0)
    as_neg = models.IntegerField(default=0)
    as_neu = models.IntegerField(default=0)
    as_query = models.IntegerField(default=0)
    as_complain = models.IntegerField(default=0)
    as_appreciation = models.IntegerField(default=0)
    as_neg_fed = models.IntegerField(default=0)
    as_pos_fed = models.IntegerField(default=0)
    total_as = models.IntegerField(default=0)
    cf_pos = models.IntegerField(default=0)
    cf_neg = models.IntegerField(default=0)
    cf_neu = models.IntegerField(default=0)
    co_query = models.IntegerField(default=0)
    co_complain = models.IntegerField(default=0)
    co_appreciation = models.IntegerField(default=0)
    co_neg_fed = models.IntegerField(default=0)
    co_pos_fed = models.IntegerField(default=0)
    total_co = models.IntegerField(default=0)
    ot_pos = models.IntegerField(default=0)
    ot_neg = models.IntegerField(default=0)
    ot_neu = models.IntegerField(default=0)
    ot_query = models.IntegerField(default=0)
    ot_complain = models.IntegerField(default=0)
    ot_appreciation = models.IntegerField(default=0)
    ot_neg_fed = models.IntegerField(default=0)
    ot_pos_fed = models.IntegerField(default=0)
    total_ot = models.IntegerField(default=0)
    campaign_status = models.IntegerField(default=0)

    def __str__(self):
        return self.status_id


class CampaignAnalysisDateRange(models.Model):
    company = models.CharField(max_length=45)
    daterange = models.CharField(max_length=45)
    num_reactions = models.IntegerField()
    num_comments = models.IntegerField()
    num_shares = models.IntegerField()
    num_likes = models.IntegerField()
    num_loves = models.IntegerField()
    num_wows = models.IntegerField()
    num_hahas = models.IntegerField()
    num_sads = models.IntegerField()
    num_angrys = models.IntegerField()
    fans_comments = models.IntegerField(default=1)
    author_comments = models.IntegerField(default=1)
    total_comments = models.IntegerField(default=1)
    response_ration = models.FloatField(default=1)
    negative = models.IntegerField(default=1)
    positive = models.IntegerField(default=1)
    neutral = models.IntegerField(default=1)
    ratiopos = models.FloatField(default=1)
    rationeg = models.FloatField(default=1)
    rationeu = models.FloatField(default=1)
    query = models.IntegerField(default=1)
    complain = models.IntegerField(default=1)
    appreciation = models.IntegerField(default=1)
    feedback = models.IntegerField(default=0)
    spam = models.IntegerField(default=1)
    wom = models.IntegerField(default=1)
    query_percentage = models.FloatField(default=1)
    complain_percentage = models.FloatField(default=1)
    appreciation_percentage = models.FloatField(default=1)
    feedback_percentage = models.FloatField(default=0)
    spam_percentage = models.FloatField(default=1)
    wom_percentage = models.FloatField(default=1)
    pi = models.IntegerField(default=1)
    pi_percentage = models.FloatField(default=0)
    npi = models.IntegerField(default=0)
    product_service = models.IntegerField(default=1)
    after_sales = models.IntegerField(default=1)
    campaign_offers = models.IntegerField(default=1)
    others = models.IntegerField(default=1)
    product_service_percentage = models.FloatField(default=1)
    after_sales_percentage = models.FloatField(default=1)
    campaign_offers_percentage = models.FloatField(default=1)
    others_percentage = models.FloatField(default=1)
    dropout_percentage = models.FloatField(default=0)
    post_user = models.ForeignKey(User, blank=True)
    postimg = models.TextField(blank=True, null=True, default='')
    ps_pos = models.IntegerField(default=0)
    ps_neg = models.IntegerField(default=0)
    ps_neu = models.IntegerField(default=0)
    ps_query = models.IntegerField(default=0)
    ps_complain = models.IntegerField(default=0)
    ps_appreciation = models.IntegerField(default=0)
    ps_neg_fed = models.IntegerField(default=0)
    ps_pos_fed = models.IntegerField(default=0)
    total_ps = models.IntegerField(default=0)
    as_pos = models.IntegerField(default=0)
    as_neg = models.IntegerField(default=0)
    as_neu = models.IntegerField(default=0)
    as_query = models.IntegerField(default=0)
    as_complain = models.IntegerField(default=0)
    as_appreciation = models.IntegerField(default=0)
    as_neg_fed = models.IntegerField(default=0)
    as_pos_fed = models.IntegerField(default=0)
    total_as = models.IntegerField(default=0)
    cf_pos = models.IntegerField(default=0)
    cf_neg = models.IntegerField(default=0)
    cf_neu = models.IntegerField(default=0)
    co_query = models.IntegerField(default=0)
    co_complain = models.IntegerField(default=0)
    co_appreciation = models.IntegerField(default=0)
    co_neg_fed = models.IntegerField(default=0)
    co_pos_fed = models.IntegerField(default=0)
    total_co = models.IntegerField(default=0)
    ot_pos = models.IntegerField(default=0)
    ot_neg = models.IntegerField(default=0)
    ot_neu = models.IntegerField(default=0)
    ot_query = models.IntegerField(default=0)
    ot_complain = models.IntegerField(default=0)
    ot_appreciation = models.IntegerField(default=0)
    ot_neg_fed = models.IntegerField(default=0)
    ot_pos_fed = models.IntegerField(default=0)
    total_ot = models.IntegerField(default=0)
    daterange_status = models.IntegerField(default=0)

    def __str__(self):
        return self.company


class KeywordAnalysis(models.Model):
    company = models.CharField(max_length=45)
    daterange = models.CharField(max_length=45)
    keyword = models.TextField(blank=True, null=True)
    post_user = models.ForeignKey(User, blank=True)
    response_ration = models.IntegerField(blank=True, default=0)
    negative = models.IntegerField(blank=True, default=0)
    positive = models.IntegerField(blank=True, default=0)
    neutral = models.IntegerField(blank=True, default=0)
    ratiopos = models.IntegerField(blank=True, default=0)
    rationeg = models.IntegerField(blank=True, default=0)
    rationeu = models.IntegerField(blank=True, default=0)
    query = models.IntegerField(blank=True, default=0)
    complain = models.IntegerField(blank=True, default=0)
    appreciation = models.IntegerField(blank=True, default=0)
    feedback = models.IntegerField(blank=True, default=0)
    feedbackneg = models.IntegerField(blank=True, default=0)
    feedbackpos = models.IntegerField(blank=True, default=0)
    spam = models.IntegerField(blank=True, default=0)
    wom = models.IntegerField(blank=True, default=0)
    query_percentage = models.IntegerField(blank=True, default=0)
    complain_percentage = models.IntegerField(blank=True, default=0)
    appreciation_percentage = models.IntegerField(blank=True, default=0)
    feedback_percentage = models.IntegerField(blank=True, default=0)
    spam_percentage = models.IntegerField(blank=True, default=0)
    wom_percentage = models.IntegerField(blank=True, default=0)
    pi = models.IntegerField(blank=True, default=0)
    npi = models.IntegerField(blank=True, default=0)
    notpi = models.IntegerField(blank=True, default=0)
    pi_percentage = models.IntegerField(blank=True, default=0)
    product_service = models.IntegerField(blank=True, default=0)
    after_sales = models.IntegerField(blank=True, default=0)
    campaign_offers = models.IntegerField(blank=True, default=0)
    others = models.IntegerField(blank=True, default=0)
    product_service_percentage = models.IntegerField(blank=True, default=0)
    after_sales_percentage = models.IntegerField(blank=True, default=0)
    campaign_offers_percentage = models.IntegerField(blank=True, default=0)
    others_percentage = models.IntegerField(blank=True, default=0)
    dropout_percentage = models.IntegerField(blank=True, default=0)
    comment_likes = models.IntegerField(blank=True, default=0)
    count = models.IntegerField(blank=True, default=0)
    ps_pos = models.IntegerField(blank=True, default=0)
    ps_neg = models.IntegerField(blank=True, default=0)
    ps_neu = models.IntegerField(blank=True, default=0)
    ps_query = models.IntegerField(blank=True, default=0)
    ps_complain = models.IntegerField(blank=True, default=0)
    ps_appreciation = models.IntegerField(blank=True, default=0)
    ps_neg_fed = models.IntegerField(blank=True, default=0)
    ps_pos_fed = models.IntegerField(blank=True, default=0)
    total_ps = models.IntegerField(blank=True, default=0)
    as_pos = models.IntegerField(blank=True, default=0)
    as_neg = models.IntegerField(blank=True, default=0)
    as_neu = models.IntegerField(blank=True, default=0)
    as_query = models.IntegerField(blank=True, default=0)
    as_complain = models.IntegerField(blank=True, default=0)
    as_appreciation = models.IntegerField(blank=True, default=0)
    as_neg_fed = models.IntegerField(blank=True, default=0)
    as_pos_fed = models.IntegerField(blank=True, default=0)
    total_as = models.IntegerField(blank=True, default=0)
    cf_pos = models.IntegerField(blank=True, default=0)
    cf_neg = models.IntegerField(blank=True, default=0)
    cf_neu = models.IntegerField(blank=True, default=0)
    co_query = models.IntegerField(blank=True, default=0)
    co_complain = models.IntegerField(blank=True, default=0)
    co_appreciation = models.IntegerField(blank=True, default=0)
    co_neg_fed = models.IntegerField(blank=True, default=0)
    co_pos_fed = models.IntegerField(blank=True, default=0)
    total_co = models.IntegerField(blank=True, default=0)
    ot_pos = models.IntegerField(blank=True, default=0)
    ot_neg = models.IntegerField(blank=True, default=0)
    ot_neu = models.IntegerField(blank=True, default=0)
    ot_query = models.IntegerField(blank=True, default=0)
    ot_complain = models.IntegerField(blank=True, default=0)
    ot_appreciation = models.IntegerField(blank=True, default=0)
    ot_neg_fed = models.IntegerField(blank=True, default=0)
    ot_pos_fed = models.IntegerField(blank=True, default=0)
    total_ot = models.IntegerField(blank=True, default=0)
    total_comments = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.daterange


class RobiProfile(models.Model):
    socialid = models.CharField(max_length=45)
    telcoid = models.CharField(max_length=45)
    name = models.CharField(max_length=45, default='')
    totoal_comment = models.IntegerField()
    pur_pattern = models.IntegerField()
    spam = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    cumSum = models.DecimalField(max_digits=5, decimal_places=2)
    sat_level = models.CharField(max_length=45)
    last_interection = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.socialid


class BLProfile(models.Model):
    socialid = models.CharField(max_length=45)
    telcoid = models.CharField(max_length=45)
    name = models.CharField(max_length=45, default='')
    totoal_comment = models.IntegerField()
    pur_pattern = models.IntegerField()
    spam = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    cumSum = models.DecimalField(max_digits=5, decimal_places=2)
    sat_level = models.CharField(max_length=45)
    last_interection = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.socialid


class GPProfile(models.Model):
    socialid = models.CharField(max_length=45)
    telcoid = models.CharField(max_length=45)
    name = models.CharField(max_length=45, default='')
    totoal_comment = models.IntegerField()
    pur_pattern = models.IntegerField()
    spam = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    cumSum = models.DecimalField(max_digits=5, decimal_places=2)
    sat_level = models.CharField(max_length=45)
    last_interection = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.socialid


class AirProfile(models.Model):
    socialid = models.CharField(max_length=45)
    telcoid = models.CharField(max_length=45)
    name = models.CharField(max_length=45, default='')
    totoal_comment = models.IntegerField()
    pur_pattern = models.IntegerField()
    spam = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    cumSum = models.DecimalField(max_digits=5, decimal_places=2)
    sat_level = models.CharField(max_length=45)
    last_interection = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.socialid


class TeleProfile(models.Model):
    socialid = models.CharField(max_length=45)
    telcoid = models.CharField(max_length=45)
    name = models.CharField(max_length=45, default='')
    totoal_comment = models.IntegerField()
    pur_pattern = models.IntegerField()
    spam = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    cumSum = models.DecimalField(max_digits=5, decimal_places=2)
    sat_level = models.CharField(max_length=45)
    last_interection = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.socialid


class Commentator(models.Model):
    socailid = models.CharField(max_length=45,primary_key=True)
    name = models.CharField(max_length=45, default='')

    @property
    def commentcount(self):
        return Comment.objects.filter(author_url=self.socailid).count()

    def __str__(self):
        return self.socailid


class CommentatorProfile(models.Model):
    socialid = models.CharField(max_length=45)
    name = models.CharField(max_length=45, default='')
    totoal_comment = models.IntegerField()
    pur_pattern = models.DecimalField(max_digits=5, decimal_places=2)
    spam = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.socialid


class MisClassifiedDataStore(models.Model):
    comment_ref = models.ForeignKey(Comment, blank=True, default='')

    def __str__(self):
        return self.comment_ref


class PostLog(models.Model):
    user = models.ForeignKey(User, blank=True, default='')
    post = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        return self.post