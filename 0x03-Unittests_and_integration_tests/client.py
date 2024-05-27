#!/usr/bin/env python3
"""
A GitHub organization client for interacting with GitHub's API.
"""
from builtins import KeyError, bool, property, staticmethod, str # type: ignore
from typing import ( # type: ignore
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)

class GithubOrgClient:
    """
    A client for GitHub organizations.
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """
        Initialize a GithubOrgClient instance.

        Parameters
        ----------
        org_name : str
            The name of the GitHub organization.
        """
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """
        Fetch and memoize the organization data.

        Returns
        -------
        Dict
            The organization data retrieved from the API.
        """
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """
        Get the URL for the organization's public repositories.

        Returns
        -------
        str
            The URL for the organization's public repositories.
        """
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """
        Fetch and memoize the repository payload data.

        Returns
        -------
        Dict
            The repository payload data retrieved from the API.
        """
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """
        Get the list of public repository names, optionally filtered by license.

        Parameters
        ----------
        license : str, optional
            The license key to filter repositories by (default is None).

        Returns
        -------
        List[str]
            A list of public repository names.
        """
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]
        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """
        Check if a repository has a specific license.

        Parameters
        ----------
        repo : Dict[str, Dict]
            The repository data.
        license_key : str
            The license key to check for.

        Returns
        -------
        bool
            True if the repository has the specified license, False otherwise.
        """
        assert license_key is not None, "license_key cannot be None"
        try:
            return access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
