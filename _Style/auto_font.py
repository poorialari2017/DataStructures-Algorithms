# _Style/auto_font.py
from IPython.display import HTML, display
import base64
import os


def setup_font():
    """تنظیم خودکار فونت برای تمام notebookها"""
    font_path = os.path.join(os.path.dirname(__file__), 'Font', 'B Nazanin.ttf')

    if os.path.exists(font_path):
        with open(font_path, 'rb') as f:
            font_data = base64.b64encode(f.read()).decode()

        css = f"""
        <style>
        @font-face {{
            font-family: 'B Nazanin';
            src: url('data:font/ttf;base64,{font_data}') format('truetype');
        }}

        .rtl-fa {{
            font-family: 'B Nazanin', 'Times New Roman', serif !important;
            text-align: right !important;
            direction: rtl !important;
            font-size: 16pt !important;  /* تغییر سایز به ۱۶ */
            line-height: 1.8 !important;
            padding: 12px;
        }}

        /* اعمال خودکار به تمام divهای فارسی */
        div[dir="rtl"] {{
            font-family: 'B Nazanin', 'Times New Roman', serif !important;
            font-size: 16pt !important;
            text-align: right !important;
            direction: rtl !important;
        }}

        /* برای عناوین */
        .rtl-fa h1, .rtl-fa h2, .rtl-fa h3, .rtl-fa h4 {{
            font-family: 'B Nazanin', 'Times New Roman', serif !important;
            text-align: right !important;
            direction: rtl !important;
        }}

        /* برای لیست‌ها */
        .rtl-fa ul, .rtl-fa ol {{
            font-family: 'B Nazanin', 'Times New Roman', serif !important;
            text-align: right !important;
            direction: rtl !important;
            font-size: 16pt !important;
        }}
        </style>
        """
        display(HTML(css))
        return True
    return False


# اجرای خودکار هنگام import
if setup_font():
    print("🎯 فونت B Nazanin (سایز ۱۶) به طور خودکار فعال شد")
else:
    print("⚠️ از فونت‌های پیش‌فرض استفاده می‌شود")