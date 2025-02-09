# GraphQL API Gateway and REST API redirector for shortening links

A service that provides URL shortening functionality through both GraphQL and REST APIs. It allows you to create shortened URLs with custom prefixes and expiration times.

## Requirements

- Python 3.12+

## Installation

```shell
pip install neojelll-api-gateway
```

## Usage

Start the server:

```shell
uv run api-gateway
```

### GraphQL API

The GraphQL API provides two main operations:

#### Query: getShortLink

Retrieves information about an existing shortened link.

**Example:**

```graphql
query {
	getShortLink(longLink: "https://www.google.com") {
		shortLink
		longLink
		expiration
	}
}
```

**Response:**

```json
{
	"data": {
		"getShortLink": {
			"shortLink": "http://localhost:15015/abc123",
			"longLink": "https://www.google.com",
			"expiration": 3600
		}
	}
}
```

#### Mutation: shortenLink

Creates a new shortened link.

**Parameters:**

- longLink: String (required) - The original URL to shorten
- expiration: Int (optional) - Time in seconds until the link expires
- prefix: String (optional) - Custom prefix for the shortened URL

**Example:**

```graphql
mutation {
	shortenLink(
		longLink: "https://www.google.com"
		expiration: 3600
		prefix: "test"
	) {
		shortLink
		longLink
		expiration
		prefix
	}
}
```

### REST API

#### Redirect Endpoint

Redirects shortened URLs to their original destinations.

**Request:**

```shell
curl -X GET http://localhost:15015/short-link
```

**Response:**

- 302: Redirect to the original URL
- 404: Link not found
- 410: Link expired

## Error Handling

[Описание возможных ошибок и их обработки]

## Limitations

[Описание ограничений сервиса, если есть]
