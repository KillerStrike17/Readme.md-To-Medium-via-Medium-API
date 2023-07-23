# Readme.md To Medium via Medium API


This repository contains a Python script that allows you to easily convert Jupyter notebooks or project Readme files into Medium blog posts using the Medium API. The script uses the `requests` library to interact with the Medium API, and it requires a valid Medium token for authentication.

## Requirements

Before running the converter script, make sure you have the following installed:

1. Python 3.x
2. All the required libraries are listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Getting Started

Follow the steps below to get started with the Jupyter/Readme to Medium Blog Post converter:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the repository directory:

```bash
cd your-repo
```

3. Create a `.env` file in the root of the repository and paste your Medium token:

```env
MEDIUM_TOKEN=YOUR_MEDIUM_TOKEN_HERE
```

4. Ensure your `.env` file is added to the `.gitignore` file, so it won't be accidentally committed and shared publicly:

```text
# .gitignore

.env
```

5. Run the Notebook.ipynb file with raw github links.

The script will handle the conversion and publish the blog post to your Medium account.

## Notes

- Make sure your Medium token is kept private and not shared with others.
- The converter script currently supports Jupyter notebooks (.ipynb) and Markdown (.md) files. Other formats are not supported at the moment.
- The script will use the first-level headings in the Jupyter notebook or Markdown file as section titles for your blog post on Medium.

## Contribution

If you find any issues or have suggestions to improve this project, feel free to open an issue or submit a pull request. Your contributions are highly welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy blogging! 🚀