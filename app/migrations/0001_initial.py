# Generated by Django 4.1 on 2024-01-18 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="핸드폰 번호"
                    ),
                ),
            ],
            options={
                "verbose_name": "사장님",
                "verbose_name_plural": "사장님",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="카테고리"
                    ),
                ),
                (
                    "barcode",
                    models.CharField(max_length=100, unique=True, verbose_name="제목"),
                ),
                ("price", models.PositiveIntegerField(verbose_name="가격")),
                ("cost", models.PositiveIntegerField(verbose_name="원가")),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="상품 이름"
                    ),
                ),
                ("description", models.TextField(verbose_name="상품 설명")),
                ("expiration_date", models.DateField(verbose_name="유통기한")),
                (
                    "size",
                    models.CharField(
                        choices=[("small", "Small"), ("large", "Large")],
                        max_length=15,
                        verbose_name="사이즈",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일시"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정시간"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.user",
                        verbose_name="사장님",
                    ),
                ),
            ],
            options={
                "verbose_name": "상품",
                "verbose_name_plural": "상품",
            },
        ),
    ]
