import requests
import nbformat
from nbconvert import MarkdownExporter

class GithubScrapper:
    def notebook_url_to_markdown(self,url: str) -> str:
        """
        Convert a Jupyter Notebook to Markdown.

        :param url: The URL of the Jupyter Notebook.
        :return: The Markdown content of the Jupyter Notebook.
        """
        # Fetch the Jupyter Notebook from the URL
        response = requests.get(url)
        notebook_content = response.text

        # Parse the notebook using nbformat
        notebook = nbformat.reads(notebook_content, as_version=nbformat.NO_CONVERT)
        metadata = notebook.get("metadata", {})

        # Convert the notebook to Markdown
        md_exporter = MarkdownExporter()
        markdown, _ = md_exporter.from_notebook_node(notebook, resources=metadata)

        return markdown
    
    def get_readme(self, url:str)->str:
        """
        Return ReadMe

        :param url: The URL of the Readme.
        :return: The Markdown content.
        """
        # Fetch the Jupyter Notebook from the URL
        response = requests.get(url)
        notebook_content = response.text
        
        return notebook_content
        