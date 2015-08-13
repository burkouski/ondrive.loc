# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20150728_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoservice',
            name='break_time_end',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='break_time_start',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='holiday_time_end',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='holiday_time_start',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='work_end',
            field=models.CharField(default=b'19', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='work_start',
            field=models.CharField(default=b'9', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='break_time_end',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='break_time_start',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='holiday_time_end',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='holiday_time_start',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='work_end',
            field=models.CharField(default=b'19', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='carwash',
            name='work_start',
            field=models.CharField(default=b'9', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='break_time_end',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043e\u0431\u0435\u0434\u0430', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='break_time_start',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0435\u0434\u0430', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='holiday_time_end',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='holiday_time_start',
            field=models.CharField(default=b'0', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='work_end',
            field=models.CharField(default=b'19', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
        migrations.AlterField(
            model_name='tireservice',
            name='work_start',
            field=models.CharField(default=b'9', max_length=5, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, choices=[(b'0', b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'1', b'0:00'), (b'2', b'1:00'), (b'3', b'2:00'), (b'4', b'3:00'), (b'5', b'4:00'), (b'6', b'5:00'), (b'7', b'6:00'), (b'8', b'7:00'), (b'9', b'8:00'), (b'10', b'9:00'), (b'11', b'10:00'), (b'12', b'11:00'), (b'13', b'12:00'), (b'14', b'13:00'), (b'15', b'14:00'), (b'16', b'15:00'), (b'17', b'16:00'), (b'18', b'17:00'), (b'19', b'18:00'), (b'20', b'19:00'), (b'21', b'20:00'), (b'22', b'21:00'), (b'23', b'22:00'), (b'24', b'23:00')]),
        ),
    ]
