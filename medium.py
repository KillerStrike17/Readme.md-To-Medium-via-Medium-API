import requests
from typing import Optional, Dict, Any, List
import json

class Medium:
    def __init__(self,token) -> None:
        self.user_id = None
        self.MEDIUM_TOKEN = token
        
    def send_request(self,url: str,method: str = "get",body: Optional[Dict[str, Any]] = None,headers: Optional[Dict[str, Any]] = None,) -> json:
        """
        Send a request to the Medium API

        :param url: The URL to send the request to
        :param method: The HTTP method to use
        :param body: The body of the request
        :param headers: The headers of the request
        :return: The response of the request
        """
        response = requests.request(method, url, json=body, headers=headers)
        return response.json()
    
    def create_post(self,
            title: str,
            content: str,
            content_format: str = "markdown",
            tags: Optional[List[str]] = None,
            canonical_url: Optional[str] = None,
            publish_status: str = "draft",
        ) -> json:
        """
        Create a post on Medium.

        :param title: The title of the post, used for SEO, doesn't appear in the actual post.
        Should be less than 100 characters.
        :param content: The content of the post.
        :param content_format: The format of the content, either `html` or `markdown`, defaults to `markdown`.
        :param tags: The tags of the post, used to classify the post. Only the first three will be used.
        Should be less than 25 characters each. Defaults to `None`.
        :param canonical_url: The original url of this content, if it was originally published elsewhere.
        Defaults to `None`.
        :param publish_status: The publish status of the post, either `public`, `draft`, or `unlisted`,
        defaults to `draft`.
        :return: The response of the request.
        """

        # Get the user_id
        if self.user_id is None:
            my_details_url = "https://api.medium.com/v1/me"
            headers = {"Authorization": f"Bearer {self.MEDIUM_TOKEN}"}

            response = self.send_request(my_details_url, headers=headers)
            self.user_id = response.get("data").get("id")

        # Ready to create a post
        url = f"https://api.medium.com/v1/users/{self.user_id}/posts"

        # set headers
        headers = {"Authorization": f"Bearer {self.MEDIUM_TOKEN}"}

        # set body
        body = {
            "title": title,
            "contentFormat": content_format,
            "content": content,
            "tags": tags,
            "canonicalUrl": canonical_url,
            "publishStatus": publish_status,
        }

        # send request with body and authentication bearer token
        response = self.send_request(url, method="post", body=body, headers=headers)
        return response

    
        
        
        