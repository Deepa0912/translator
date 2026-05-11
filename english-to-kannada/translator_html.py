from deep_translator import GoogleTranslator
from datetime import datetime
import webbrowser
import os

# Initialize translator
translator = GoogleTranslator(source='en', target='kn')

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English to Kannada Translator</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        
        .container {{
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 900px;
            width: 100%;
            padding: 40px;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 20px;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            color: #333;
            margin-bottom: 10px;
        }}
        
        .header p {{
            color: #666;
            font-size: 1.1em;
        }}
        
        .translation-item {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-left: 5px solid #667eea;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            transition: transform 0.3s ease;
        }}
        
        .translation-item:hover {{
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
        }}
        
        .translation-item .timestamp {{
            font-size: 0.85em;
            color: #999;
            margin-bottom: 10px;
        }}
        
        .translation-item .label {{
            font-weight: bold;
            color: #667eea;
            font-size: 0.95em;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .translation-item .english {{
            background: white;
            padding: 12px;
            border-radius: 5px;
            margin-bottom: 15px;
            color: #333;
            font-size: 1.05em;
            line-height: 1.6;
        }}
        
        .translation-item .kannada {{
            background: white;
            padding: 12px;
            border-radius: 5px;
            color: #764ba2;
            font-size: 1.1em;
            font-weight: 500;
            line-height: 1.6;
            font-family: 'Arial Unicode MS', Arial, sans-serif;
        }}
        
        .empty-state {{
            text-align: center;
            color: #999;
            padding: 40px;
            font-size: 1.1em;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #999;
            font-size: 0.9em;
        }}
        
        @media (max-width: 600px) {{
            .container {{
                padding: 20px;
            }}
            
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .translation-item {{
                padding: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌐 English to Kannada Translator</h1>
            <p>Translations displayed below</p>
        </div>
        
        <div class="translations">
            {translations_html}
        </div>
        
        <div class="footer">
            <p>Last updated: {timestamp}</p>
        </div>
    </div>
</body>
</html>
"""

# Build translations HTML
translations_list = []

print("===================================")
print(" English to Kannada Translator ")
print("===================================\n")

while True:
    text = input("Enter English text (or type 'exit' to quit): ")
    
    if text.lower() == "exit":
        print("\nGenerating HTML output...")
        break
    
    if not text.strip():
        print("Please enter some text.\n")
        continue
    
    try:
        translated = translator.translate(text)
        
        print(f"\nKannada Translation:")
        print(translated)
        print()
        
        # Add to translations list
        translations_list.append({
            'english': text,
            'kannada': translated,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
    except Exception as e:
        print(f"Error: {e}\n")

# Generate HTML content
if translations_list:
    translations_html = ""
    for item in translations_list:
        translations_html += f"""
        <div class="translation-item">
            <div class="timestamp">✓ {item['timestamp']}</div>
            <div class="label">English</div>
            <div class="english">{item['english']}</div>
            <div class="label">ಕನ್ನಡ (Kannada)</div>
            <div class="kannada">{item['kannada']}</div>
        </div>
        """
else:
    translations_html = '<div class="empty-state">No translations yet. Please run the program and add some translations.</div>'

# Final HTML
final_html = html_template.format(
    translations_html=translations_html,
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

# Write to file
output_file = "translations.html"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"✓ HTML output saved to: {output_file}")
print(f"\nTotal translations: {len(translations_list)}")

# Open in browser
if translations_list:
    webbrowser.open('file://' + os.path.realpath(output_file))
    print("Opening in browser...")

print("Translator Closed.")
