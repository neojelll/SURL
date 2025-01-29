<p align="center">
  <a href="https://github.com/neojelll/surl" target="_blank"><img src="docs/images/surl-logo.png" width="250" alt="surl logo" /></a>
</p>

<p align="center">
  <b><a href="https://neojelll/surl" target="_blank">SURL</a> - service for fast and convenient shortening of long links into neat short links</b>
</p>

<p align="center">
	<img alt="GitHub Release" src="https://img.shields.io/github/v/release/neojelll/surl?include_prereleases&display_name=release&style=flat">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/neojelll/surl/.github%2Fworkflows%2Fpublish.yml?style=flat">
	<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.12-blue?style=flat">
	<img alt="Coveralls" src="https://img.shields.io/coverallsCoverage/github/neojelll/surl?style=flat">
	<img alt="GitHub License" src="https://img.shields.io/github/license/neojelll/surl?style=flat">
	<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/neojelll/surl?style=social">
</p>

## Description

A SURL is a handy tool, long long hair, complex URLs in short places, easy to remember links. Ideal for routing traffic on your social media pages, email campaigns and websites. Simplify your links and track their performance in one place!

## Project Focus

- Make the process of link shortening as simple as possible and user-friendly

- Provide data analytics via a shortened link

## Use Cases

### General

- A user submits a request with a link that he wants to shorten using cURL

  Parameter|Default value|Description
  -|-|-
  expiration | 1 day | link validity time
  prefix | empty string | link prefix

- In response he receives a short link
- When using a short link, it will be redirected to the original one
- If the link has expired, the user will receive a static page in response with information that the link did not exist or is no longer valid

### WebUI

All the same as described in General, using SPA (Single Page Application) WebUI

### Telegram

All the same as described in General, using a bot in Telegram

## Architecture

### Containers Diagram

![Container](architecture/diagrams/container-diagram.png)
