# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-31 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='appearance',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u6587\u8d28\u5f6c\u5f6c'), (2, '\u5c0f\u9e1f\u4f9d\u4eba'), (3, '\u9633\u5149\u5e05\u6c14'), (4, '\u96cd\u5bb9\u534e\u8d35'), (5, '\u5176\u4ed6')], default='0', max_length=60, verbose_name='\u5916\u8c8c'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='blood_type',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, 'A\u578b'), (2, 'B\u578b'), (3, 'O\u578b'), (4, 'AB\u578b'), (5, '\u5176\u4ed6')], default='0', max_length=32, verbose_name='\u8840\u578b'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bodystyle',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u7626'), (2, '\u82d7\u6761'), (3, '\u80a5\u80d6'), (4, '\u5176\u4ed6')], default='0', max_length=60, verbose_name='\u4f53\u578b'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='career',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u5728\u6821\u5b66\u751f'), (2, '\u8ba1\u7b97\u673a/\u4e92\u8054\u7f51/IT'), (3, '\u7535\u5b50/\u534a\u5bfc\u4f53/\u4eea\u5668\u4eea\u8868'), (4, '\u901a\u4fe1\u6280\u672f'), (5, '\u9500\u552e'), (6, '\u5176\u4ed6')], default='0', max_length=60, verbose_name='\u804c\u4e1a'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='constellation',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u767d\u7f8a\u5ea7'), (2, '\u91d1\u725b\u5ea7'), (3, '\u53cc\u5b50\u5ea7'), (4, '\u5de8\u87f9\u5ea7'), (5, '\u72ee\u5b50\u5ea7'), (6, '\u5904\u5973\u5ea7'), (7, '\u5929\u79e4\u5ea7'), (8, '\u5929\u874e\u5ea7'), (9, '\u5c04\u624b\u5ea7'), (10, '\u6469\u7faf\u5ea7'), (11, '\u6c34\u74f6\u5ea7'), (12, '\u53cc\u9c7c\u5ea7')], default='0', max_length=12, verbose_name='\u661f\u5ea7'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='dating_type',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u670b\u53cb'), (2, '\u77e5\u5df1'), (3, '\u604b\u7231'), (4, '\u7ed3\u5a5a')], default='0', max_length=60, verbose_name='\u4ea4\u53cb\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='facestyle',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u5706\u8138'), (2, '\u957f\u8138'), (3, '\u65b9\u8138'), (4, '\u5176\u4ed6')], default='0', max_length=60, verbose_name='\u8138\u578b'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='glamour_place',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u773c\u775b'), (2, '\u9f3b\u5b50'), (3, '\u8138'), (4, '\u6ca1\u6709')], default='0', max_length=60, verbose_name='\u9b45\u529b\u90e8\u4f4d'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='haircolor',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u9ed1\u8272'), (2, '\u767d\u8272'), (3, '\u91d1\u8272'), (4, '\u5149\u5934'), (5, '\u5176\u4ed6')], default='1', max_length=60, verbose_name='\u53d1\u8272'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='hairstyle',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u5782\u76f4\u957f\u53d1'), (2, '\u5377\u66f2\u957f\u53d1'), (3, '\u4e2d\u7b49\u53d1\u578b'), (4, '\u77ed\u53d1'), (5, '\u5176\u4ed6')], default='0', max_length=60, verbose_name='\u53d1\u578b'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='have_car',
            field=models.BooleanField(choices=[(True, '\u5df2\u8d2d\u8f66'), (False, '\u672a\u8d2d\u8f66')], default=False, verbose_name='\u8d2d\u8f66\u60c5\u51b5'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='have_kid',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u65e0\u5c0f\u5b69'), (2, '\u6709\uff0c\u548c\u6211\u4f4f\u4e00\u8d77'), (3, '\u6709\uff0c\u6709\u65f6\u548c\u6211\u4f4f\u4e00\u8d77'), (4, '\u6709\uff0c\u4e0d\u548c\u6211\u4f4f\u4e00\u8d77')], default='0', max_length=32, verbose_name='\u662f\u5426\u6709\u5c0f\u5b69'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='height',
            field=models.CharField(choices=[[160, '160CM'], [161, '161CM'], [162, '162CM'], [163, '163CM'], [164, '164CM'], [165, '165CM'], [166, '166CM'], [167, '167CM'], [168, '168CM'], [169, '169CM'], [170, '170CM'], [171, '171CM'], [172, '172CM'], [173, '173CM'], [174, '174CM'], [175, '175CM'], [176, '176CM'], [177, '177CM'], [178, '178CM'], [179, '179CM'], [180, '180CM'], [181, '181CM'], [182, '182CM'], [183, '183CM'], [184, '184CM'], [185, '185CM'], [186, '186CM'], [187, '187CM'], [188, '188CM'], [189, '189CM'], [190, '190CM'], [191, '191CM'], [192, '192CM'], [193, '193CM'], [194, '194CM'], [195, '195CM'], [196, '196CM'], [197, '197CM'], [198, '198CM'], [199, '199CM'], [200, '200CM']], default='160', max_length=12, verbose_name='\u8eab\u9ad8'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='house_situation',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u6682\u672a\u8d2d\u623f'), (2, '\u9700\u65f6\u8d2d\u623f'), (3, '\u5df2\u8d2d\u623f'), (4, '\u4e0e\u4eba\u5408\u79df'), (5, '\u72ec\u81ea\u79df\u623f'), (6, '\u4e0e\u7236\u6bcd\u540c\u4f4f'), (7, '\u5176\u4ed6')], default='0', max_length=120, verbose_name='\u4f4f\u623f\u60c5\u51b5'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='img',
            field=models.ImageField(null=True, upload_to='static/imgs/img/', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='marray_state',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u672a\u5a5a'), (2, '\u5df2\u5a5a'), (3, '\u79bb\u5f02'), (4, '\u4e27\u5076')], default='0', max_length=32, verbose_name='\u5a5a\u59fb\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='national',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u6c49\u65cf'), (2, '\u85cf\u65cf'), (3, '\u8499\u53e4\u65cf'), (4, '\u58ee\u65cf'), (5, '\u56de\u65cf'), (6, '\u7ef4\u543e\u5c14\u65cf'), (7, '\u671d\u9c9c\u65cf'), (8, '\u82d7\u65cf'), (9, '\u9ece\u65cf'), (10, '\u5176\u4ed6')], default='1', max_length=60, verbose_name='\u540d\u65cf'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nationality',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u4e2d\u56fd\u5927\u9646'), (2, '\u4e2d\u56fd\u53f0\u6e7e'), (3, '\u4e2d\u56fd\u9999\u6e2f'), (4, '\u4e2d\u56fd\u6fb3\u95e8'), (5, '\u5370\u5ea6\u5c3c\u897f\u4e9a'), (6, '\u97e9\u56fd'), (7, '\u671d\u9c9c'), (8, '\u65e5\u672c'), (9, '\u8d8a\u5357'), (10, '\u8001\u631d'), (11, '\u6cf0\u56fd'), (12, '\u67ec\u57d4\u5be8'), (13, '\u7f05\u7538'), (14, '\u6587\u83b1'), (15, '\u4e1c\u5e1d\u6c76'), (16, '\u9a6c\u6765\u897f\u4e9a')], default='1', max_length=60, verbose_name='\u56fd\u7c4d'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='personality',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u6d6a\u6f2b\u8ff7\u4eba'), (3, '\u627f\u53d7\u7a33\u91cd'), (4, '\u98ce\u8da3\u5e7d\u9ed8'), (5, '\u4e50\u5929\u8fbe\u89c2'), (6, '\u6d3b\u6cfc\u53ef\u7231'), (7, '\u5fe0\u539a\u8001\u5b9e'), (8, '\u6566\u539a\u5bb3\u7f9e'), (9, '\u6e29\u67d4\u4f53\u8d34'), (10, '\u591a\u6101\u5584\u611f'), (11, '\u65b0\u6f6e\u65f6\u5c1a'), (12, '\u70ed\u8fa3\u52a8\u611f'), (13, '\u8c6a\u653e\u4e0d\u7f81')], default='0', max_length=60, verbose_name='\u4e2a\u6027'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='salary',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '2000\u5143\u4e00\u4e0b'), (2, '2000-5000\u5143'), (3, '5000-10000\u5143'), (4, '10000-20000\u5143'), (5, '20000\u5143\u4ee5\u4e0a')], default='0', max_length=120, verbose_name='\u85aa\u8d44'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weight',
            field=models.CharField(choices=[[200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM'], [200, '200CM']], default='50', max_length=10, verbose_name='\u4f53\u91cd'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='zodiac',
            field=models.CharField(choices=[(0, '\u8bf7\u9009\u62e9'), (1, '\u9f20'), (2, '\u725b'), (3, '\u864e'), (4, '\u5154'), (5, '\u9f99'), (6, '\u86c7'), (7, '\u9a6c'), (8, '\u7f8a'), (9, '\u7334'), (10, '\u9e21'), (11, '\u72d7'), (12, '\u732a')], default='0', max_length=12, verbose_name='\u751f\u8096'),
        ),
    ]
