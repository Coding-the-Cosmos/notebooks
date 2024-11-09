import os
import re
import json
from IPython.display import display, Markdown

class I18N:
    _instance = None  # Private class variable to hold the singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(I18N, cls).__new__(cls)
        return cls._instance

    def __init__(self, path='locale', locale='en_CA', images_url=''):
        """
        Initialize the I18N class with the path to the locale files and the desired locale.

        Parameters:
        - path: The path to the locale files. Default is 'locale'.
        - locale: The desired locale. Default is 'en_CA'.
        - images_url: The URL to prepend to image paths in Markdown files. Default is ''
        """

        # Initialize only if it hasn't been done for the singleton instance
        if not hasattr(self, 'initialized'):
            self.path = path
            self.locale = locale
            self.images_url = images_url
            self.translations = self._load_translations()
            self.initialized = True  # Avoid reinitializing in case of multiple instantiation

    def gettext(self, key) -> str:
        """
        Get the translation for a given key. If the key is not found, return the key itself.

        Parameters:
        - key: The key to look up in the translations dictionary.

        Returns:
        - The translation if the key is found, or the key itself if not found
        """
        return self.translations.get(key, key)

    def md(self, filename) -> None:
        """
        Display the content of a Markdown file in the current language.

        Parameters:
        - filename: The name of the Markdown file to display (without the .md extension)

        Returns:
        - None
        """
        
        try:
            from google.colab import output # type: ignore
            output.no_vertical_scroll()
        except ImportError:
            pass

        md_content = self._load_markdown(filename)
        if self.images_url != '':
            md_content = re.sub(r'<img src="media/', f'<img src="{self.images_url}/', md_content)

        display(Markdown(md_content))

    def _load_translations(self) -> dict:
        """
        Load the translations for the current locale.

        Returns:
        - A dictionary containing the translations
        """

        filepath = os.path.join(self.path, self.locale, 'messages.json')
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'Warning: Translation file not found for locale {self.locale}. Using default (en_CA).')
            return {}

    def _load_markdown(self, filename: str) -> str:
        """
        Load the content of a Markdown file in the current language.

        Parameters:
        - filename: The name of the Markdown file to load (without the .md extension)

        Returns:
        - The content of the Markdown file as a string
        """
        filepath = os.path.join(self.path, self.locale, f'content/{filename}.md')
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f'Warning: File not found for {filepath}')
            return ''