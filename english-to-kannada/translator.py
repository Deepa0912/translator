from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='kn')

print("===================================")
print(" English to Kannada Translator ")
print("===================================")

while True:
    text = input("\nEnter English text (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("Translator Closed.")
        break

    try:
        translated = translator.translate(text)

        print("\nKannada Translation:")
        print(translated)

    except Exception as e:
        print("Error:", e)