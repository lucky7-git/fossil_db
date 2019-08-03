from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # ID
    col01_fossil_ID = models.CharField(
        verbose_name='ID',
        max_length=25,
       # primary_key=True,
        blank=True,
        null=True,    
    )

    # 分類CD
    col02_category_CD = models.CharField(
        verbose_name='分類CD',
        max_length=16,
        blank=True,
        null=True,
    )

    # 名称 
    col03_fossil_name = models.CharField(
        verbose_name='名称',
        max_length=255,
        blank=True,
        null=True,
    )

    # 愛称 
    col04_nickname = models.CharField(
        verbose_name='愛称',
        max_length=255,
        blank=True,
        null=True,
    )

    # 学名 
    col05_binomen = models.CharField(
        verbose_name='学名',
        max_length=255,
        blank=True,
        null=True,
    )

    # 界 
    col06_kingdom = models.CharField(
        verbose_name='界',
        max_length=50,
        blank=True,
        null=True,
    )

    # 門 
    col07_phylum = models.CharField(
        verbose_name='門',
        max_length=50,
        blank=True,
        null=True,
    )

    # 亜門 
    col08_subphylum = models.CharField(
        verbose_name='亜門',
        max_length=50,
        blank=True,
        null=True,
    )

    # 綱 
    col09_lass_nm = models.CharField(
        verbose_name='綱',
        max_length=50,
        blank=True,
        null=True,
    )

    # 亜綱 
    col10_subclass = models.CharField(
        verbose_name='亜綱',
        max_length=50,
        blank=True,
        null=True,
    )

    # 下綱 
    col11_infraclass = models.CharField(
        verbose_name='下綱',
        max_length=50,
        blank=True,
        null=True,
    )

    # 上目 
    col12_superorder = models.CharField(
        verbose_name='上目',
        max_length=50,
        blank=True,
        null=True,
    )

    # 目 
    col13_order = models.CharField(
        verbose_name='目',
        max_length=50,
        blank=True,
        null=True,
    )

    # 亜目 
    col14_suborder = models.CharField(
        verbose_name='亜目',
        max_length=50,
        blank=True,
        null=True,
    )

    # 下目 
    col15_infraorder = models.CharField(
        verbose_name='下目',
        max_length=50,
        blank=True,
        null=True,
    )

    # 類 
    col16_group = models.CharField(
        verbose_name='類',
        max_length=50,
        blank=True,
        null=True,
    )

    # 上科 
    col17_superfamily = models.CharField(
        verbose_name='上科',
        max_length=50,
        blank=True,
        null=True,
    )

    # 科 
    col18_family = models.CharField(
        verbose_name='科',
        max_length=50,
        blank=True,
        null=True,
    )

    # 亜科 
    col19_subfamily = models.CharField(
        verbose_name='亜科',
        max_length=50,
        blank=True,
        null=True,
    )

    # 属 
    col20_genus = models.CharField(
        verbose_name='属',
        max_length=50,
        blank=True,
        null=True,
    )

    # 亜属 
    col21_subgenus = models.CharField(
        verbose_name='亜属',
        max_length=50,
        blank=True,
        null=True,
    )

    # 発掘部位 
    col22_part = models.CharField(
        verbose_name='発掘部位',
        max_length=255,
        blank=True,
        null=True,
    )

    # 部位サイズ 
    col23_part_size = models.CharField(
        verbose_name='部位サイズ',
        max_length=255,
        blank=True,
        null=True,
    )

    # 推定体長 
    col24_estimate_length = models.CharField(
        verbose_name='推定体長',
        max_length=50,
        blank=True,
        null=True,
    )

    # 産地CD
    col25_product_CD = models.CharField(
        verbose_name='産地CD',
        max_length=2,
        blank=True,
        null=True,
    )

    # 郵便番号
    col26_zip_CD = models.CharField(
        verbose_name='郵便番号',
        max_length=8,
        blank=True,
        null=True,
    )

    # 産地(県) 
    col27_prefecture = models.CharField(
        verbose_name='産地(県)',
        max_length=8,
        blank=True,
        null=True,
    )

    # 産地(市) 
    col28_city = models.CharField(
        verbose_name='産地(市)',
        max_length=10,
        blank=True,
        null=True,
    )

    # 地層
    col29_stratum = models.CharField(
        verbose_name='地層',
        max_length=255,
        blank=True,
        null=True,
    )

    # 発見年
    col30_discovery_date = models.CharField(
        verbose_name='発見年',
        max_length=8,
        blank=True,
        null=True,
    )

    # 発見者
    col31_discoverer = models.CharField(
        verbose_name='発見者',
        max_length=40,
        blank=True,
        null=True,
    )

    # 発見者職業
    col32_discoverer_job = models.CharField(
        verbose_name='発見者職業',
        max_length=40,
        blank=True,
        null=True,
    )

    # 発表区分
    col33_announced_flag = models.CharField(
        verbose_name='発表区分',
        max_length=8,
        blank=True,
        null=True,
    )
    
    # 発表年
    col34_announced_date = models.CharField(
        verbose_name='発表年',
        max_length=8,
        blank=True,
        null=True,
    )

    # 報告者
    col35_reporter = models.CharField(
        verbose_name='報告者',
        max_length=40,
        blank=True,
        null=True,
    )

    # 報告者職業
    col36_reporter_job = models.CharField(
        verbose_name='報告者職業',
        max_length=40,
        blank=True,
        null=True,
    )

    # 地質年代CD
    col37_geologic_CD = models.CharField(
        verbose_name='地質年代CD',
        max_length=8,
        blank=True,
        null=True,
    )

    # 累代
    col38_eon = models.CharField(
        verbose_name='累代',
        max_length=50,
        blank=True,
        null=True,
    )

    # 代
    col39_era = models.CharField(
        verbose_name='代',
        max_length=50,
        blank=True,
        null=True,
    )

    # 紀
    col40_period = models.CharField(
        verbose_name='紀',
        max_length=50,
        blank=True,
        null=True,
    )

    # 世
    col41_epoch = models.CharField(
        verbose_name='世',
        max_length=50,
        blank=True,
        null=True,
    )

    # 期
    col42_age = models.CharField(
        verbose_name='期',
        max_length=50,
        blank=True,
        null=True,
    )

    # 年代
    col43_year_ago = models.CharField(
        verbose_name='年代',
        max_length=50,
        blank=True,
        null=True,
    )

    # 概要
    col44_outline = models.CharField(
        verbose_name='概要',
        max_length=255,
        blank=True,
        null=True,
    )

    # 詳細
    col45_details = models.TextField(
        verbose_name='詳細',
        blank=True,
        null=True,
    )

    # 所蔵館
    col46_collect_museum  = models.CharField(
        verbose_name='所蔵館',
        max_length=50,
        blank=True,
        null=True,
    )

    # 標本番号
    col47_sumple_number  = models.CharField(
        verbose_name='標本番号',
        max_length=50,
        blank=True,
        null=True,
    )

    # 参考文献1
    col48_works_cited１  = models.CharField(
        verbose_name='参考文献1',
        max_length=255,
        blank=True,
        null=True,
    )

    # 参考文献2
    col49_works_cited2  = models.CharField(
        verbose_name='参考文献2',
        max_length=255,
        blank=True,
        null=True,
    )

    # 参考文献3
    col50_works_cited3  = models.CharField(
        verbose_name='参考文献3',
        max_length=255,
        blank=True,
        null=True,
    )


    # 添付データ1
    col51_attach1 = models.CharField(
     #   upload_to='media/' #upload_to/%Y/%m/%d/',
        verbose_name='添付データ1',
        max_length=255,
        blank=True,
        null=True,
     #   validators=[FileExtensionValidator(['png', ])],
    )

    #image = models.ImageField(
     #   upload_to='files/',
     #   verbose_name='添付画像',
    #    height_field='url_height',
    #    width_field='url_width',
    #)
    #url_height = models.IntegerField(
    #    editable=False,
    #)

    #url_width = models.IntegerField(
    #    editable=False,
    #)

    # 添付データ1コメント
    col52_attach1_comment  = models.CharField(
        verbose_name='添付データ1コメント',
        max_length=255,
        blank=True,
        null=True,
    )

    # 添付データ2
    col53_attach2 = models.CharField(
    #    upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付データ2',
     #   validators=[FileExtensionValidator(['png', ])],
        max_length=255,
        blank=True,
        null=True,
    )

    # 添付データ2コメント
    col54_attach2_comment  = models.CharField(
        verbose_name='添付データ2コメント',
        max_length=255,
        blank=True,
        null=True,
    )

    # 添付データ3
    col55_attach3 = models.CharField(
    #    upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付データ3',
    #    validators=[FileExtensionValidator(['png', ])],
        max_length=255,
        blank=True,
        null=True,
    )

    # 添付データ3コメント
    col56_attach3_comment  = models.CharField(
        verbose_name='添付データ3コメント',
        max_length=255,
        blank=True,
        null=True,
    )

    # 更新日
    col57_last_update  = models.CharField(
        verbose_name='更新日',
        max_length=8,
        blank=True,
        null=True,
    )

 #   def __str__(self):
 #       return self.Item

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = '化石DB'
        verbose_name_plural = '化石DB'